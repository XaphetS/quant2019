
# coding: utf-8

# # 1.python基础试题

# 1.1 python 中boolean、float 和 int 分别表示什么？

# In[ ]:


int 表示整型bool表示布尔类型str表示字符串类型


# 1.2  设计求1-2+3-4+5 ... 99的所有数的和

# In[1]:


#!/usr/bin/env python
# -*- coding:utf-8 -*-
#求1-2+3-4+5...99的所有数的和
"""
给start赋值为1，sum赋值为0，当start的赋值小于100的时候while循环为真
temp的赋值等于start和2的余数，如果temp的赋值等于1，sum的赋值就等于
sum加start的赋值（余数为1，start就是奇数），否则sum的赋值就等于sum减start的
赋值（余数不为1就为0，start就是偶数），start重新赋值
等于start加1，一直加到start的赋值等于99，while循环为假！打印sum
"""
start = 1
sum = 0
while start <100:
    temp = start % 2
    if temp ==1:
        sum = sum + start
    else:
        sum = sum - start
    #print(start)
    #sum = sum + 1
    start += 1
print(sum)


# 1.3  将字符串 s="yoyo" 转换成列表

# In[2]:


s = "yoyo"
list(s)


# # 2. python进阶基础试题

# 2.1     for i in range(1,100)[2::3][-10:]: 
# 
#                 print i 
#                 
#         理解这段代码，并说出它是如何取数的

# In[4]:


for i in range(1,100)[2::3][-10:]:

            print (i) 


# In[ ]:


从100开始倒数每隔3取一个数 取10个


# 2.2 使用init 实例化时自动运行  分别计算单只股票最高价和收盘价两个时间点差值问题,可统一为one、two两个时间点,其最高价和收盘价赋值为 one(15,7) two(66,20)

# In[5]:


def func(a,b):
     c = a-b
    print('one_dif ', c)
    print('two_dif ', c)


# # 3. pandas数据处理试题

# 3.1 如何查看列名、怎么对数据转置

# 3.2 读取data里的600029这只股票的DataFrame,将其收盘价转换成用Numpy的Array格式，并用talib计算10日EMA值，返回ndarray的最后五个值

# In[4]:


import talib.abstract as ta

df_ma = pd.DataFrame({name: ta.MA(value, 10) for name, value in PN.iteritems()})
print(df_ma.tail())


# In[5]:





# 3.3 读取sz50.xlsx的['600029.XSHG','600050.XSHG','601318.XSHG']的全数据做成Panel

# In[6]:


from datetime import datetime
import pandas as pd
symbol=['600036.XSHG','600050.XSHG','601318.XSHG']
data_dict = {}
for s in symbol:
    data =  pd.read_excel('sz50.xlsx',sheetname=s, index_col='datetime')
    data_dict[s] = data.loc['2017-03-21':'2017-05-10']
PN = pd.Panel(data_dict)
print(PN)


# 3.4把Panel转成ndim为3的Numpy，然后用array的切片读取ndim为2的三只股票最近20天的收盘价

# In[7]:





# 3.5 建立一个5*5的矩阵，值从0到24

# In[8]:


from numpy import *
a = arange(25).reshape(5, 5)
a

