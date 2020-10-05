import pymysql
import datetime

# MySQL Connection 연결
#conn = pymysql.connect(host='35.223.121.143', user='alertjjm', password='sdr2936',
#                       db='attend', charset='utf8')
conn = pymysql.connect(host='localhost', user='root', password='sdr2936',
                       db='attend', charset='utf8')
# Connection 으로부터 Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

# SQL문 실행
sqllog = "select * from log join device on log.device_id = device.device_id where is_processed=0"
curs.execute(sqllog)

# 데이타 Fetch
logrows = curs.fetchall()

# SQL문 실행
sqllog = "select * from attendance" #향후에는 where entertime between today, today로 고치기
curs.execute(sqllog)

# 데이타 Fetch
attendrows = curs.fetchall()

#updatesql="""update attendance set exit_time = %s where personal_id = %s and room_id = %s and enter_time= %s"""
updatesql="""update attendance set exit_time = %s where `index`= %s"""

insertsql="insert into attendance(personal_id,room_id,enter_time, exit_time) values (%s, %s, %s, %s)"
logupdate="update log set is_processed = 1 where node_id = %s and device_id = %s and RSSI = %s"
for logrow in logrows:
    print(logrow)
    count=0
    for attendrow in attendrows:
        if(logrow['personal_id']==attendrow['personal_id']):
            if(logrow['time']>attendrow['exit_time'] and (logrow['time']-attendrow['exit_time']).seconds<=900):
                datestr=logrow['time'].strftime("%Y-%m-%d %H:%M:%S")
                #curs.execute(updatesql,(datestr, attendrow['personal_id'],attendrow['room_id'],attendrow['enter_time'].strftime("%Y-%m-%d %H:%I:%S")))
                curs.execute(updatesql,(datestr, attendrow['index']))
                curs.execute(logupdate, (logrow['node_id'], logrow['device_id'], logrow['RSSI']))
                attendrow['exit_time']=logrow['time']
                print("update")
                count+=1
                break
    if count==0:
        enterstr=(logrow['time']+datetime.timedelta(seconds=-600)).strftime("%Y-%m-%d %H:%M:%S")
        exitstr=logrow['time'].strftime("%Y-%m-%d %H:%M:%S")
        curs.execute(insertsql,(logrow['personal_id'],logrow['node_id'],enterstr,exitstr))
        curs.execute(logupdate,(logrow['node_id'],logrow['device_id'],logrow['RSSI']))
        attendrow['enter_time'] = logrow['time']+datetime.timedelta(seconds=-600)
        attendrow['exit_time']=logrow['time']
        attendrows.append({'index': 99, 'personal_id': logrow['personal_id'], 'room_id': logrow['node_id'], 'enter_time': logrow['time']+datetime.timedelta(seconds=-600), 'exit_time': logrow['time']})
        print("insert")
conn.commit()
# Connection 닫기
conn.close()