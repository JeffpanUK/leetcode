#-*-coding:utf-8-*-
#!usr/bin/env python
import numpy as np

class DP(object):
  def __init__(self, prices):
    self.BUY = -1
    self.SEL = 1
    self.COL = 0
    self.prices = prices
    buy = [-1 for _ in range(len(prices))]
    sel = [1 for _ in range(len(prices))]
    col = [0 for _ in range(len(prices))]
    self.actions = np.hstack((buy,sel,col)) 
  
  def stock1(self):
  #用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。 如果只允许进行一次交易，也就是说只允许买一支股票并卖掉，求最大的收益。
    #DP算法
    lowest = self.prices[0]
    max_p = 0
    buy_d = 0
    buy_dp = 0
    sel_d = 0
    for d, p in enumerate(self.prices):
      if p < lowest:
        lowest = p 
        buy_dp = d 
      profit = p - lowest
      if profit > max_p:
        max_p = profit
        buy_d = buy_dp
        sel_d = d
    print("Maximum Profit: %d"%max_p)
    print("Buy Date: %d"%buy_d)
    print("Sel Date: %d"%sel_d)
 
  def stock2(self):
  #用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。交易次数不限，但一次只能交易一支股票，也就是说手上最多只能持有一支股票，求最大收益。
    #贪心算法
    total = 0
    for d, p in enumerate(self.prices):
      print("Day %d, Price %d"%(d,p))
      if d > 0:
        if p > self.prices[d-1]:
          print("Buy Day: %d"%(d-1))
          print("Sell Day: %d, profit: +%d"%(d, p-self.prices[d-1]))
          total += p-self.prices[d-1]
        else:
          print("Cool Down")
      print("------------------------")
    print("Total Profit: %d"%total)
 
  def stock3(self):
  #用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。最多交易两次，手上最多只能持有一支股票，求最大收益
    #DP算法
    Profit = []
    action = []
    for i in range(len(self.prices)):
      stocks = [self.prices[:i], self.prices[i:]]
      secProfit = []
      secAction = []
      for f, s in enumerate(stocks):
        lowest = self.prices[0]
        max_p = 0
        buy_d = 0
        buy_dp = 0
        sel_d = 0
        for d, p in enumerate(s):
          if p < lowest:
            lowest = p 
            buy_dp = d 
          profit = p - lowest
          if profit > max_p:
            max_p = profit
            buy_d = buy_dp
            sel_d = d
        secProfit.append(max_p)
        secAction.append((buy_d+i*f, sel_d+i*f))
      Profit.append(secProfit)
      action.append(secAction)
      
    totalProfit = list(map(lambda x: x[0]+x[1], Profit))
    maxProfit = max(totalProfit)
    index = totalProfit.index(maxProfit)
    print("Maximum Profit: %d"%maxProfit)
    print("Action 1: Buy at Day %d(%d CNY) and sell at Day %d(%d CNY)"%(action[index][0][0], self.prices[action[index][0][0]], action[index][0][1], self.prices[action[index][0][1]]))
    print("Action 2: Buy at Day %d(%d CNY) and sell at Day %d(%d CNY)"%(action[index][1][0], self.prices[action[index][1][0]], action[index][1][1], self.prices[action[index][1][1]]))
 
def test_stock1():
  prices = [1,2,3,0,2,3,1,10,1,2,-1,3,0,11,12,5,2,1,0,10]
  dp = DP(prices)
  dp.stock1()
  for d, p in enumerate(prices):
    print("[%d] %d"%(d,p))
 
def test_stock2():
  prices = [1,2,3,0,2,3,1,10,1,2,-1,3,0,11,12,5,2,1,0,10]
  dp = DP(prices)
  dp.stock2()
  
def test_stock3():
  prices = [1,2,3,0,2,3,1,10,1,2,-1,3,0,11,12,5,2,1,0,10]
  dp = DP(prices)
  dp.stock3()
  
if __name__ == "__main__":
  #test_stock1()
  #test_stock2()
  test_stock3()