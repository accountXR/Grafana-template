import math
import pandas as pd
import pymysql
import csv

db = pymysql.connect(
    host="127.0.0.1",
    user="slurm",
    password="slurm_mysql_password",
    database="slurm_acct_db",
    port=3306,
    charset='utf8'
)
sql = '''select id_job, account, state, time_submit, time_start, time_end from hpc_job_table WHERE time_submit BETWEEN (UNIX_TIMESTAMP(now())-604800) AND UNIX_TIMESTAMP(now())'''
data = pd.read_sql(sql,db)

# 去除time_start为0的行
time_start_zero = data[data['time_start'] == 0].index
data.drop(time_start_zero, inplace=True)

# 去除time_end为0的行
time_end_zero = data[data['time_end'] == 0].index
data.drop(time_end_zero, inplace=True)

# state == 3为COMPLTED，state == 1024为running，保留
state_err = data[data['state'].isin([4,5,6,7])].index
data.drop(state_err, inplace=True)

data['time_wait'] = data['time_start'] - data['time_submit']

# 去除time_wait超过一天的数据
time_wait_out_1day = data[data['time_wait'] > 86400].index
data.drop(time_wait_out_1day, inplace=True)

data['time_run'] = (data['time_end'] - data['time_start']) / 3600

# 将data按照account排序
sort_data = data.sort_values(by=['account'])

pd.DataFrame.to_csv(sort_data,"mysql.csv",encoding="utf_8_sig")
