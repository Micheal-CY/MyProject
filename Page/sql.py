import random
from datetime import date, timedelta, time

import pymysql
from sshtunnel import SSHTunnelForwarder

from Page.random_time import get_user_id, Type

perf = 'perftest'
zld_test = "zldtest"
days = 6    # 循环多少天


def UserMysql(db):
    d = date(2017, 11, 9)   # 起始时间
    server = SSHTunnelForwarder(
        ssh_address_or_host=('dev.zlddata.cn', 22),  # 指定ssh登录的跳转机的address
        ssh_username='root',  # 跳转机的用户
        ssh_password='Hdfds*&2156gda',  # 跳转机的密码
        remote_bind_address=('127.0.0.1', 3306))
    server.start()
    myConfig = pymysql.connect(
        user="root",
        passwd="Hkdff*79231lgfj",
        host="127.0.0.1",
        db=db,
        port=server.local_bind_port)
    cursor =myConfig.cursor()
    start_time = 0
    for z in range(1, 6):
        day = timedelta(days=z)
        print(d+day)
        for i in range(1, get_user_id(zld_test)):
            start_time = start_time + random.randint(60, 3600)
            a = time.localtime(start_time)
            change_time = time.strftime("%H:%M:%S", a)
            sql = """insert into
            project_attendanceinstant(day, time, type, attendance_machine_id, user_id )
            VALUES ('%s','%s','%d',5,'173')""" % (d + day, change_time, Type())
            print(sql)
            rel = cursor.execute(sql)
            myConfig.commit()
            # sleep(0.5)
            print(rel)
            if int(time.strftime("%H", a)) == 23 and int(time.strftime("%M", a)) >= 30:
                print('a')
                continue
    # myConfig.commit()
    # 关闭数据库连接
    cursor.close()
if __name__ == '__main__':
    UserMysql(zld_test)