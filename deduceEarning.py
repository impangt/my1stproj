#!/usr/bin/python
import numpy as np
import pandas as pd
import StockAccount as sa

mysa = sa.StockAccount()

def getbuypolicieslist():
    buyplist = ['N days go up',
                'N days go down',
                'Bottom Railway Signal']
    return buyplist

def getsellpolicieslist():
    sellplist = ['Stop lossing',
                 'Get profits after earning ',
                 'Go down from hight',
                 'Cannot go back lossing',
                 'Top Railway Signal']
    return sellplist

# read days data from cvs file
def readDailyData(filename):  # , starday, endday):
    df = pd.read_csv(filename)
    df = df.set_index('date')
    df = df.ix[:, ['open', 'high', 'low', 'close', 'vol', 'turn']]
    return df

# Buy policy : buy when there are continually N(default N=3) days that the price go up ( open price < close price )
def buyPolicy_upfewdays(LOpen=[], LClose=[]):
    isbuypoint = True
    n = len(LOpen)
    for i in range(0, n):
        if LOpen[i] >= LClose[i]:
            isbuypoint = False
            break
    return isbuypoint

def buyPolicy_dowfewdays(LOpen=[], LClose=[]):
    isbuypoint = True
    n = len(LOpen)
    for i in range(0, n):
        if LOpen[i] <= LClose[i]:
            isbuypoint = False
            break
    return isbuypoint

def buyPolicy_bottomrailway(LOpen=[], LClose=[], LHigh=[], LLow=[]):
    isbuypoint = False

    if (LOpen[-2] > LClose[-2]) and (LOpen[-1] < LClose[-1]):
        if (LHigh[-1]-LLow[-1])/(LHigh[-1] - LClose[-1]) < 3.0:
            isbuypoint = False

        d1 = LOpen[-2] - LClose[-2]
        d2 = LClose[-1] - LOpen[-1]
        if d2 >= d1:
            isbuypoint = True

    return isbuypoint
############################################################################
# Sell policy 1: sell when we loss capital over N%, default N = 10
def sellPolicy_stoploss(buypoint, currentprice, lossrate=10):
    if lossrate < 0 or lossrate > 100:
        print('WARNING: input loss rate should be in the range of 0 to 100')
        return False

    if buypoint > currentprice:
        c1 = (buypoint - currentprice) / buypoint * 100.0
        if c1 >= lossrate:
            return True

    return False

# Sell policy 2: sell when we get enough profits
def sellPolicy_getprofits(buypoint, currentprice, uprate):
    if (buypoint < currentprice) and (buypoint > 0.0):
        c2 = (currentprice - buypoint) / buypoint * 100.0
        if c2 >= uprate:
            return True
    return False

# s Sell policy4: sell when the price turns down from earning to lossing
def sellPolicy_cannotgobacklossing(buyprice, highpoint, currentprice):
    if highpoint < buyprice:
        return False
    elif buyprice <= currentprice *(1-mysa.taxes):
        return True
    return False

# s Sell policy3: sell when the price turns down N rate from the highest point
def sellPolicy_downfromhight(highpoint, currentprice, downrate):
    if highpoint < currentprice or downrate <= 0:
        return False
    elif highpoint > 0:
        c3 = (highpoint - currentprice) / highpoint * 100.0
        if c3 >= downrate:
            return True
    return False

# Sell policy 5: when there is a top railway signal emerges
def sellPolicy_toprailway(LOpen=[], LClose=[]): #, LHigh=[], LLow=[]):
    isbuypoint = False
    if (LOpen[-2] < LClose[-2]) and (LOpen[-1] > LClose[-1]):
        isbuypoint = True

    return isbuypoint

####################################################################
## main loop for policies
####################################################################
def runBackTrace(dataframe, buyplist, sellplist):
    mysa.getinidata()
    predays = mysa.daysgoup
    i = predays
    while i < len(dataframe.index):
        todayopen = dataframe.iloc[i, 0]
        todayclose = dataframe.iloc[i, 3]
        todayhigh = dataframe.iloc[i, 1]
        todaylow = dataframe.iloc[i, 2]

        L1 = dataframe.iloc[i - predays:i, 0]  # open
        L2 = dataframe.iloc[i - predays:i, 3]  # close
        L3 = dataframe.iloc[i - predays:i, 1]  # high
        L4 = dataframe.iloc[i - predays:i, 2]  # low

        t = i
        if mysa.status:  # we can sell
            if mysa.highestpoint < todayhigh:
                mysa.highestpoint = todayhigh

            # sell policies frame work
            issell = True
            if sellPolicy_stoploss(mysa.buyprice, todaylow, mysa.stoplossrate) and sellplist[0]:  # cut loss policy
                sprice = mysa.buyprice*(1.0-mysa.stoplossrate/100)
                print('sell:stoploss ', dataframe.index[i], end='')
                i = i + predays - 1  # if sell out today for cut loss, we will not buy in n(predays) days
            elif sellPolicy_getprofits(mysa.buyprice, todayclose, mysa.stopearnrate) and sellplist[1]:  # sell for getting profits
                sprice = mysa.buyprice * (1.0 + mysa.stopearnrate/100)
                print('>>>sell:getprofits ', dataframe.index[i], end='')
                i = i + predays * 2  # if sell out today for cut earning, we will not buy in the next few days
            elif sellPolicy_downfromhight(mysa.highestpoint, todayhigh, mysa.turndownrate) and sellplist[2]:
                sprice = mysa.highestpoint * (1.0 - mysa.turndownrate / 100)
                print('sell:downfromhight ', mysa.highestpoint, mysa.turndownrate, dataframe.index[i], end='')
            elif sellPolicy_cannotgobacklossing(mysa.buyprice, mysa.highestpoint, todaylow) and sellplist[3]:
                sprice = todaylow * (1.0 + mysa.taxes)
                print('sell:cannotlossing ', mysa.highestpoint, mysa.turndownrate, dataframe.index[i], end='')
            elif sellPolicy_toprailway(L1,L2) and sellplist[4]:
                sprice = todaylow * (1.0 + mysa.taxes)
                print('sell:toprailway ', dataframe.index[i], L1[-1],L2[-1],todayopen, end='')
                i = i + 4
            else:
                issell = False

            if issell:
                mysa.sellAction(sprice)
                dayindex = dataframe.index[t]
                dataframe.at[dayindex, 'sell'] = sprice
                print('--sell', mysa.stocks, ' shares at price', dataframe.at[dayindex, 'sell'], ' all money=', mysa.moneyihave)
                mysa.status = False
                mysa.stocks = 0
        else:  # we can buy
            isbuy = True
            # buy policies frame work
            if buyPolicy_upfewdays(L1, L2) and buyplist[0]:  # buy policy
                print('buy:upfewdays', dataframe.index[i], end='')
            elif buyPolicy_dowfewdays(L1, L2) and buyplist[1]: # add other buy policy action as this.
                print('buy:downfewdays', dataframe.index[i], end='')
            elif buyPolicy_bottomrailway(L1, L2, L3, L4) and buyplist[2]:  # buy when bottom railway signal emerges.
                print('buy:bottom_railway', dataframe.index[i], L1[-1],L2[-1],todayopen, end='')
            else:
                isbuy = False

            if isbuy:
                mysa.buyAction(mysa.moneyihave, (todayhigh + todaylow) / 2)
                dayindex = dataframe.index[i]
                dataframe.at[dayindex, 'buy'] = (todayhigh + todaylow) / 2
                mysa.status = True
                print(' buy', mysa.stocks, ' shares at price', (todayhigh + todaylow) / 2, ' all money=', mysa.stocks * (todayopen + todayclose) / 2 + mysa.moneyihave)
        i = i + 1
    # caculate the profit in the last day
    lastday = len(dataframe.index)-1
    incomes = dataframe.iloc[lastday, 3] * mysa.stocks*(1-mysa.taxes) + mysa.moneyihave
    print('----incomes =', incomes,' tax is',mysa.taxes, dataframe.iloc[lastday, 3] * mysa.stocks*mysa.taxes,' ---------')
    mysa.accountReset()  # 计算完毕后将账户信息恢复为初始状态，以便再次计算
    return incomes

# originData = readDailyData('data\\SH#603588.txt')
# originData['buy'] = 0.0
# originData['sell'] = 0.0
# dataframe = originData.iloc[499:567,]
# buypl = [1,0]
# sellpl = [1,1,1,0]
# # print(dataframe.head(5))
# incomes = runBackTrace(dataframe,buypl,sellpl)
# print(dataframe)
# print('My profits = ', incomes)
