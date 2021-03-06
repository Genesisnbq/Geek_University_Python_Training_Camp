import pandas as pd

# pip install xlrd
# 导入excel文件
excel1 = pd.read_excel(r'1.xlsx')

excel1

# 指定导入哪个Sheet
pd.read_excel(r'1.xlsx', sheet_name=0)  # 第几个表

# 支持其他常见类型
pd.read_csv(r'book_utf8.csv', sep=' ', nrow=10, encoding='utf-8')

# 导入 txt文件
pd.read_table(r'file.txt', sep=' ')

import pymysql

sql = 'SELECT * FROM tb1'
conn = pymysql.connect('localhost', 'root', 'root', 'python_geek', 'charset=utf8')
df = pd.read_sql(sql, conn)

# 熟悉数据
# 显示前几行
excel1.head(3)

# 行列数量
excel1.shape

# 详细信息
excel1.info()
excel1.describe()
