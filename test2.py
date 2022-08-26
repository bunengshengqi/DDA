# panda的merge操作
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# 创建两个DataFrame
df1 = DataFrame({'key': ['x', 'y', 'z', 'x'], 'data_set_1': ['1', '2', '3', '4']})
print(df1)

df2 = DataFrame({'key': ['x', 'b', 'c'], 'data_set_2': ['4', '5', '6']})
print(df2)
# merge操作是为了取出df1和df2中同时具有的'x'，即相同名称的columns

pd1 = pd.merge(df1, df2)

print(pd1)


# merge里的'on'方法
# on方法默认为None，如果on使用on='key',返回结果同上，同样会出现两边都有的'key'
pd2 = pd.merge(df1, df2, on='key')
print(pd2)
# on方法默认为None，如果on使用on='data_set_1', 则会报错。

# how  方法
# how默认的方法是inner，结果同上
pd3 = pd.merge(df1, df2, how='inner')
print(pd3)

# 使用left方法，会保留df1所有的columns和row，df2会过来并且使用NaN做一个补全
print('---------------------')
pd4 = pd.merge(df1, df2, how='left')
print(pd4)


# 使用right和left的方法类似，不过是以df2为基准。
print('********************')
pd5 = pd.merge(df1, df2, how='right')
print(pd5)

# 使用outer方法，会保留df1和df2所有的columns和values,并且会使用nan做一个补全

print('+++++++++++++++++')
pd6 = pd.merge(df1, df2, how='outer')
print(pd6)