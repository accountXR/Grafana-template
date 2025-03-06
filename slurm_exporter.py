from prometheus_client import start_http_server
from prometheus_client import Gauge
import subprocess
import time
import os
import pandas as pd
import pymysql

slurm_submit_job_count = Gauge('slurm_submit_job_count', 'Total number of tasks submitted by slurm', ['type'])

slurm_squeue  = Gauge('slurm_squeue', 'Job information in the queue', ['JOBID', 'PARTITION', 'NAME', 'USER', 'ST', 'TIME', 'NODES', 'NODELIST'])

def get_slurm_submit_job_count():
        db = pymysql.connect(host="127.0.0.1",
                             user="slurm",
                             password="slurm_mysql_password",
                             database="slurm_acct_db",
                             port=3306,
                             charset='utf8')
        sql = '''select count(*) from hpc_job_table'''
        df = pd.read_sql(sql,db)
        number = df.iat[0,0]
        slurm_submit_job_count.labels('slurm').set(int(number))

def get_slurm_squeue():
        count = 1
        command = 'squeue -a'          #可以直接在命令行中执行的命令
        r = os.popen(command)       #执行该命令
        slurm_squeue.clear()
        for line in r:
            line = line.rstrip()
            if not line: continue        #判断line是不是空行
            info = line.split()
            try:
                    nodelist = ' '.join(info[7:])
                    slurm_squeue.labels(JOBID = info[0],
                                        PARTITION = info[1],
                                        NAME = info[2],
                                        USER = info[3],
                                        ST = info[4],
                                        TIME = info[5],
                                        NODES = info[6],
                                        NODELIST = nodelist).set(count)
            except Exception as exp:
                    with open("error.txt", "a") as fd:
                            fd.write(f"[ {time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))} ] {line}\n")

if __name__=='__main__':
	# Start up the server to expose the metrics
	start_http_server(9300)
	# Generate some requests.
	while True:
                get_slurm_submit_job_count()
                get_slurm_squeue()
                time.sleep(10)
