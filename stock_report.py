#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

def checkFileSize( file ):                              #检查读取文件是否错误
    content = file.read()
    if(len(content) > 1000 ):
        print('upload file is error')
        exit(-1)
    else:
        print('checkFileSize passed')

def checkDetail(fileList):                              #检查读取的文件明细有没有变更或者错误
    fExamp = open('example.txt', 'r')
    fileListExamp = fExamp.readlines()
    detailNameExamp = fileListExamp[8]
    detailName = fList[8]
    if ( detailName != detailNameExamp ):
        print('upload file is different with example file')
        exit(-1)
    else:
        print('checkDetail passed')

######数据读取
f = open('1.txt', 'r')

fList = f.readlines()


department = fList[1][6:]                       #营业部名称
shareholder = fList[2][3:]                      #股东
fundBallance = fList[3][5:14]               #资金余额
fundBallance = float(fundBallance)
stockMarketValue = fList[4][17:]        #股票市值
stockMarketValue = float(stockMarketValue)
stockTotalAssets = fList[5][22:]         #股票账户总 资 产
stockTotalAssets = float(stockTotalAssets)
detailName = re.split(r'\s+', fList[8])                         #股票明细名称


datailDataLine = 9
stockCount = 0
detailItem = []
while( len(fList[datailDataLine + stockCount]) > 2 ):                  #股票明细
    m = re.split(r'\s+', fList[datailDataLine + stockCount])
    detailItem.append(m)
    stockCount = stockCount + 1

reportDate = fList[datailDataLine + stockCount + 2]                #报告生成日期
reportDate = reportDate[5:15]

otherAssets = 20400                          #外部资产
totalAssets = stockTotalAssets + otherAssets    #总资产

checkFileSize(f)
checkDetail(fList)
f.close()
######数据处理######
reportDate_outP = reportDate + '========'
detailName_outP = []
detailName_outP.append(detailName[1])
detailName_outP.append(detailName[2])
detailName_outP.append(detailName[3])
detailName_outP.append(detailName[7])
detailName_outP.append(detailName[9])
detailName_outP.append(detailName[10])
detailName_outP.append('资金占比')

detailItem_outP = []

for x in range(0,stockCount):
    detailItem_oneItem = []
    detailItem_oneItem.append(detailItem[x][1])         #证券代码
    detailItem_oneItem.append(detailItem[x][2])         #证券名称
    detailItem[x][3] = float(detailItem[x][3])
    detailItem_oneItem.append(detailItem[x][3])         #股票余额
    detailItem[x][7] = float(detailItem[x][7])
    detailItem_oneItem.append(detailItem[x][7])         #成本价
    detailItem[x][9] = float(detailItem[x][9])
    detailItem_oneItem.append(detailItem[x][9])         #市价
    detailItem[x][10] = float(detailItem[x][10])
    detailItem_oneItem.append(detailItem[x][10])        #市值
    detailItem_oneItem.append(round(detailItem[x][10]/totalAssets, 3)) #资产占比
    detailItem_outP.append(detailItem_oneItem)


stockProportionTotalAssets = round(stockTotalAssets/totalAssets ,3)

#print(stockMarketValue,stockTotalAssets )
#print(totalAssets ) 
#print(reportDate_outP)
#print(detailName )
print(reportDate_outP)
print(detailName_outP ) 
for x in range(0,stockCount):
    print(detailItem_outP[x])

print(stockProportionTotalAssets)
print(totalAssets)
######数据存储######


