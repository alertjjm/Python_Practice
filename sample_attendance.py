import pymysql
import datetime

# MySQL Connection 연결 - 내 GCP 디비 credential 혹시 실제 디비에 하려면 이거로
#conn = pymysql.connect(host='35.223.121.143', user='alertjjm', password='sdr2936',
#                       db='attend', charset='utf8')
#로컬 디비고, 각자 자신 로컬에 세팅해놓은 디비 정보 입력 - 당연히 더미데이터는 각자 원하는데이터 넣어야함
conn = pymysql.connect(host='localhost', user='root', password='sdr2936',
                       db='attend', charset='utf8')
# Connection 으로부터 Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor) #딕셔너리 형태로 칼럼명-value로 리턴해줌

# SQL문 실행
#log테이블에서 is_processed=0(처리안된 데이터) 들을 싹다 가져와라 향후에는 오늘꺼만 처리하게 바꿔야겠죠 어차피 옛날데이터는 처리 해도 의미없응께
#글고 디바이스정보-로그정보 통해서 personal id알아내야돼서 join해서 갖고옴
sqllog = "select * from log join device on log.device_id = device.device_id where is_processed=0"
curs.execute(sqllog)

# 데이타 Fetch
logrows = curs.fetchall()

# SQL문 실행
sqllog = "select * from attendance" #이거도 향후에는 where entertime between today, today로 고쳐야겠죠? 어제껀 이미 다 처리돼있을거니까 오늘꺼만 처리하게여
curs.execute(sqllog)

# 데이타 Fetch
attendrows = curs.fetchall()

#이건 나중에 쓸 쿼리 미리넣어둔것
#attendance테이블에서 pk인 index가지고 exit_time 갱신하기 - 포맷은 정수든 float이든 datetime이든 무조건 %s로 해야함 그리고 index는 예약어라서 쓰려면 그리스 quote ` 으로 묶어쓰기!
updatesql="""update attendance set exit_time = %s where `index`= %s"""
#attendance테이블에 새로운 row를 추가해주는 쿼리
insertsql="insert into attendance(personal_id,room_id,enter_time, exit_time) values (%s, %s, %s, %s)"
#log테이블에서 index기반으로 처리한 패킷들 ins_proessed=1로 바꿔주기
logupdate="update log set is_processed = 1 where `index`= %s"
#로그 row들 순회
for logrow in logrows:
    print(logrow)
    count=0 #hit개수 저장한것임 다 돌고나서도 0이면 새 row insert해주려구
    #이제는 attendance에서 fetch해온 row들 순회
    for attendrow in attendrows:
        #당연히 log에서갖고온 row랑 attendance의 row가 personal_id가 같아야겠져?
        if(logrow['personal_id']==attendrow['personal_id']):
            #로그의 time이랑 각 attend row의 exit_time을 비교해서 15분 이내에 뭔가가 찍혀있으면
            if(logrow['time']>attendrow['exit_time'] and (logrow['time']-attendrow['exit_time']).seconds<=900):
                #datetime.datetime 포맷이니까 %s로 바꿔주려구~ 앞으로 이거쓰면됨 datetime 포맷변환은
                datestr=logrow['time'].strftime("%Y-%m-%d %H:%M:%S")
                #attendance테이블 갱신하기
                curs.execute(updatesql,(datestr, attendrow['index']))
                #log테이블에서 처리했다고 바꿔주기
                curs.execute(logupdate, (logrow['index']))
                #매번 갱신할때마다 select * 해서 가져오면 오버헤드 오지니까 맨처음에 갖고온 list 재활용할거고 그거 재활용하려면 그 list도 알맞게 갱신해줘야겠져?
                attendrow['exit_time']=logrow['time']
                print("update")
                count+=1
                break
    #attendance를 순회했는데도 암것도 없다? -> 출석찍힌지 15분 지났다던가 아얘 새로왔던가겠죠? 그니까 이젠 갱신이 아니라 삽입을 해줍시다
    if count==0:
        enterstr=(logrow['time']+datetime.timedelta(seconds=-600)).strftime("%Y-%m-%d %H:%M:%S")
        exitstr=logrow['time'].strftime("%Y-%m-%d %H:%M:%S")
        #새 행을 삽입해줍니다
        curs.execute(insertsql,(logrow['personal_id'],logrow['node_id'],enterstr,exitstr))
        # log테이블에서 처리했다고 바꿔주기
        curs.execute(logupdate, (logrow['index']))
        #이건뭐냐면 새로 삽입할때 그래도 예의상 9시 5분에 찍혔으면 아 그래 너 8시 55분~9시 5분에 온거로 해줄께 라고 10분 빼서 엔터나임에 넣고 원래 시간을 엑싯에 넣는겁니다
        attendrow['enter_time'] = logrow['time']+datetime.timedelta(seconds=-600)
        attendrow['exit_time']=logrow['time']
        #앞에서 얘기했듯이 list갱신해줘야되는데 이건 갱신할 item이없으니까 append로 한줄 추가해줍시다
        attendrows.append({'index': 99, 'personal_id': logrow['personal_id'], 'room_id': logrow['node_id'], 'enter_time': logrow['time']+datetime.timedelta(seconds=-600), 'exit_time': logrow['time']})
        print("insert")
#이 모든건 commit을 하기 전까진 디비에 반영이 안됩니다
#깃허브처럼 이것도 커밋합시다 - push는 안해도됨~
conn.commit()
# Connection 닫기
conn.close()