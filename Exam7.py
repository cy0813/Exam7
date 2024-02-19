# -*- coding: utf-8 -*-
from selenium import webdriver


driver=webdriver.Chrome()

url1='https://www.google.com/maps/search/'

while True:
    
    msg=[]

    url2=input('請輸入查詢字串:')

    if url2!='end':
         urls=url1+url2
         msg.append(url2)
         
         driver.get(urls)
    else:
         break

for items in msg:
    
    print('以查詢字串:'+items)
    print('\n')
    
print('共'+str(len(msg))+'筆!')



















