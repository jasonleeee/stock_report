#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkFileSize( file ):
    content = file.read()
    return (len(content) < 1000 )


f = open('1.txt', 'r')

fList = f.readlines()
department = fList[1][6:]           #营业部名称
shareholder = fList[2][3:]          #股东
fundBallance = fList[3][5:14]       #资金余额
stockMarketValue = fList[4][17:]    #股票市值
totlaAssets = fList[5][22:]         #总 资 产


print(fList[8])

f.close()


