#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

######数据读取
f = open('1.txt', 'r')

fList = f.readlines()


department = fList[1][6:]                       #营业部名称
shareholder = fList[2][3:]                      #股东
fundBallance = fList[3][5:14]               #资金余额
fundBallance = float(fundBallance)
#stockMarketValue = fList[4][17:]        #股票市值
stockMarketValue = re.findall(r'\d+\.?\d', fList[4])
stockMarketValue = stockMarketValue[1]
#stockMarketValue = float(stockMarketValue)
stockTotalAssets = fList[5][22:]         #股票账户总 资 产
stockTotalAssets = float(stockTotalAssets)
detailName = re.split(r'\s+', fList[8])                         #股票明细名称

print(fundBallance)
print(stockMarketValue)
print(stockTotalAssets)
