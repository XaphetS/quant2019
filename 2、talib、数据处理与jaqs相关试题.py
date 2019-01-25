
# coding: utf-8

# # 4. 数据计算与统计试题

# 4.1计算股票600104与600518的相关系数、spearman排序相关性与30天滚动的五日收益协方差

# In[5]:


from jaqs_fxdayu.research import SignalDigger
obj = SignalDigger(output_folder='./output',
                   output_format='pdf')

# 处理因子 计算目标股票池每只股票的持有期收益，和对应因子值的quantile分类
obj.process_signal_before_analysis(signal=dv.get_ts("pb"),
                                   price=dv.get_ts("close_adj"),
                                   high=dv.get_ts("high_adj"), # 可为空
                                   low=dv.get_ts("low_adj"),# 可为空
                                   group=dv.get_ts("sw1"),# 可为空
                                   n_quantiles=5,# quantile分类数
                                   mask=mask,# 过滤条件
                                   can_enter=can_enter,# 是否能进场
                                   can_exit=can_exit,# 是否能出场
                                   period=15,# 持有期
                                   benchmark_price=dv.data_benchmark, # 基准价格 可不传入，持有期收益（return）计算为绝对收益
                                   commission = 0.0008,
                                   )
signal_data = obj.signal_data
signal_data.head()


# In[7]:





# In[8]:


from jaqs_fxdayu.research.signaldigger.analysis import analysis
result = analysis(signal_data, is_event=False, period=15)


# In[9]:


print("——ic分析——")
print(result["ic"])
print("——选股收益分析——")
print(result["ret"])
print("——最大潜在盈利/亏损分析——")
print(result["space"])


# 4.2
# 读取600104.XSHG的股票日线
# 
# 利用正确的方法将日K线聚合成周K线
# 
# 将周K线画出来

# In[2]:





# 4.3 读取股票601857数据，计算股票回报率，判断样本在2017-01-01,到2017-12-31，有没有服从正态分布，并判断样本均值是否为0

# In[3]:


# 分组分析
from jaqs_fxdayu.research.signaldigger import performance as pfm
ic = pfm.calc_signal_ic(signal_data, by_group=True)
mean_ic_by_group = pfm.mean_information_coefficient(ic, by_group=True)


# In[4]:


from jaqs_fxdayu.research.signaldigger import plotting

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plotting.plot_ic_by_group(mean_ic_by_group)
plt.show()


# 4.4 用Pandas的递归函数计算EMA与DEMA，对比talib的EMA与DEMA
# 1. 根据以上的算法，利用Pandas的ewm方法计算601901.XSHG以10天为周期的EMA，再算出DEMA。
# 2. 用talib计算601901.XSHG以10天为周期的EMA，再算出DEMA。
# 3. 打印两个结果的最后5个数据

# In[10]:


import matplotlib.pyplot as plt
obj.create_full_report()
plt.show()


# In[11]:


import matplotlib.pyplot as plt
obj.create_full_report()
plt.show()


# # 5.分析工具

# 数据时间：  'start_date': 20140101, 'end_date': 20180101, '

# 5.1（大致输出结果有下图）
# 
# 5.1.1可视化比较CCI、Divert（习题定义）、pb的10日变化率、vwap_adj的10日变化率 这4个因子在5日、30日、60日持有期下的平均IC和IC_IR
# 
# 5.1.2挑选上题中5日IC_IR最大的3个因子进行因子组合（注意需对因子进行去极值和z-score标准化处理，最终的组合因子也需要进行z-score标准化处理），并用柱状图比较各组合方法生成的因子与原因子在5日持有期下的IC和IC_IR；调用指标分析和可视化分析的方法，查看ic_weight方法合成的因子绩效，保存该合成方法下绩效最好quantile的选股结果

# In[46]:





# In[47]:





# ### 比较组合前和组合后的因子在5日持有期下的表现（统一到2014年9月后进行比较）

# In[54]:





# In[55]:





# In[56]:





# In[57]:





# In[58]:





# In[59]:





# 
# 5.2. 优化动量因子momentum：vwap_adj的n日变化率中的参数n（2<=n<=10）。优化目标是10日持有期的IC的IR。（要求：进行样本内优化，优化所用数据时段20140101~20170101，查看样本外20170101~表现，大致输出以下结果）

# In[70]:





# 样本外可视化

# In[72]:




