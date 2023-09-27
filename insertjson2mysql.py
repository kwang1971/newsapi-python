import pymysql
import json
from pymysql.converters import escape_string  # escape_string函数用来转义json类型数据


# 连接数据库
conn = pymysql.connect(
    host="localhost", user="root", password="mysql", database="togeek"
)

# 使用Python生成json数据类型
params = {"name": ["zhangsan", "lisi"], "age": [23, 45]}
d_params = json.dumps(params)  #

# 建立cursor游标
cursor = conn.cursor()

# 写要执行的sql语句
tsql = "insert into data_m_called_records (model_id, date_time, in_data, out_data) values(1, current_timestamp(), '{json1}', '{json2}')"  # 原sql语句
sql = tsql.format(
    json1=escape_string(d_params), json2=escape_string(d_params)
)  # escape_string方法转义json类型数据

# 执行sql语句并提交
cursor.execute(sql)
conn.commit()

# 关闭连接
cursor.close()
conn.close()
