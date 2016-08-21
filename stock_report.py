#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

detailItem = [{}]

def checkFileSize( file ):
    content = file.read()
    if(len(content) > 1000 ):
        print('upload file is error')
    else:
        print('checkFileSize passed')

def checkDetail(fileList):
    fExamp = open('example.txt', 'r')
    fileListExamp = fExamp.readlines()
    detailNameExamp = fileListExamp[8]
    detailName = fList[8]
    if ( detailName != detailNameExamp ):
        print('upload file is different with example file')
    else:
        print('checkDetail passed')


f = open('1.txt', 'r')

fList = f.readlines()
department = fList[1][6:]           #营业部名称
shareholder = fList[2][3:]          #股东
fundBallance = fList[3][5:14]       #资金余额
stockMarketValue = fList[4][17:]    #股票市值
totlaAssets = fList[5][22:]         #总 资 产
detailName = fList[8]

line = 9
print(len(fList[6]))

while( len(fList[line]) > 2 ):
    m = re.split(r'\s+', fList[line])
    detailItem[line - 9]['stockNumb'] =  m[1]
    print(detailItem[line - 9]['stockNumb'])
    line = line + 1

print(line)

checkFileSize(f)
checkDetail(fList)


print(stockMarketValue,totlaAssets)
print(totlaAssets) 
print(fList[8])

f.close()


