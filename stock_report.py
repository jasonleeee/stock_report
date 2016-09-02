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

#营业部名称
department = fList[1][6:]                       
#股东
shareholder = fList[2][3:]                      
#资金余额            
fundBallance = re.findall(r'\d+\.?\d', fList[3])
fundBallance = fundBallance[0]
fundBallance = float(fundBallance)
#股票市值
stockMarketValue = re.findall(r'\d+\.?\d', fList[4])
stockMarketValue = stockMarketValue[1]
stockMarketValue = float(stockMarketValue)
#股票账户总 资 产
stockTotalAssets = re.findall(r'\d+\.?\d', fList[5])
stockTotalAssets = stockTotalAssets[1]
stockTotalAssets = float(stockTotalAssets)
#股票明细名称
detailName = re.split(r'\s+', fList[8])                         

#股票明细数据
datailDataLine = 9
stockCount = 0
detailItem = []
while( len(fList[datailDataLine + stockCount]) > 2 ):                  
    m = re.split(r'\s+', fList[datailDataLine + stockCount])
    detailItem.append(m)
    stockCount = stockCount + 1
    
#报告生成日期
reportDate = fList[datailDataLine + stockCount + 2]                
reportDate = reportDate[5:15]

#外部资产
otherAssets = 30400
#总资产
totalAssets = stockTotalAssets + otherAssets    

checkFileSize(f)
checkDetail(fList)
f.close()

######数据处理######
#日期
reportDate_outP = reportDate + '========'
#明细项目名称
detailName_outP = []
detailName_outP.append(detailName[1])
detailName_outP.append(detailName[2])
detailName_outP.append(detailName[3])
detailName_outP.append(detailName[7])
detailName_outP.append(detailName[9])
detailName_outP.append(detailName[10])
detailName_outP.append('资金占比')

#明细数据
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

#总股票资产占比
stockProportionTotalAssets = round(stockMarketValue/totalAssets ,3)


print(reportDate_outP)
print(detailName_outP )
print(len(detailName_outP))
for x in range(0,stockCount):
    print(detailItem_outP[x])

print(stockProportionTotalAssets)
print(totalAssets)
######数据存储######

f_DataStorage = open(reportDate+ '.txt' , 'w')

f_DataStorage.write(reportDate_outP + '\n')
for x in range(0, len(detailName_outP)):
    f_DataStorage.writelines(detailName_outP[x] + '\t')
f_DataStorage.writelines('\n')

for x in range(0, stockCount):
    for y in range(0, len(detailItem_outP[x]) - 1):
        f_DataStorage.writelines(str(detailItem_outP[x][y]) + '\t')
    f_DataStorage.writelines(str(round(detailItem_outP[x][y + 1] * 100, 3)) + '%\n')

f_DataStorage .writelines('股票持仓比例: ' + str(round(stockProportionTotalAssets * 100, 3)) + '%\n')
f_DataStorage.writelines('上证: ' + '\n')
f_DataStorage.writelines('总资产: ' + str(totalAssets) + '\n')

f_DataStorage.close()









