# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:18:07 2020

@author: DELL
"""

import requests
import time
import xlsxwriter

url="https://www.xiaomiyoupin.com/api/gateway/detail"
flag=0
max=20
result=[]
q=list(range(110000,999999))#创建一个队列
while len(q):
    n=q.pop(0)#取第一个进行判断并删除
    value = {"groupName": "details",
             "groupParams": [[n]],
             "methods": [],
             "version": "1.0.0",
             "debug": "false"}
    try:
        r = requests.post(url,json = value)
        request = r.json()
        cde=request['code']
        if flag!=max:#对标记进行判断，如果有20次连续访问失败就结束
            if cde!=0:
                flag=flag+1
                pass
            else:
                data=request['data']['goods']['shareInfo']['contentMap']['title']
                flag=0
                print(data)
                result.append(data)#把商品名存入result中
        else:
            break
    except Exception as e:
        q.append(n)#出问题的放到最后
    time.sleep(0.1)
    
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write_row('A1',['序号','名称'])
for num in range(0,len(result)):
    s='A'+str(num+2)
    worksheet.write_row(s,[str(num+1),result[num]])
workbook.close()
   
















 
