# SQLite 연동
# Python Database 연동 
# Table Create / Insert

import sqlite3 #기본 라이브러리
import datetime # 날짜 호출하는 기본 모듈

# 삽입 날짜 생성 
# print('sqlite3.version : ',sqlite3.version)현재 날짜
now= datetime.datetime.now()
print("now:", now)
# 현재 시간 변수에 저장
nowDatetime=now.strftime("%y/%m-%d %H:%M:%S")
print("nowDateTime :",nowDatetime)
# sqlite3 version 확인
print('sqlite3.version : ',sqlite3.version)
print('sqlite3.sqlite_version : ',sqlite3.sqlite_version)

# DB Create & Auto commit (변경 사항 반영)
# Commit의 반대가 Rollback

conn=sqlite3.connect('./resource/database.db',isolation_level=None)

# Cursor : 파일을 읽는 부분을 의미 
c=  conn.cursor()
print('Curosr Type :', type(c))


# 테이블 생성 
# Data Type : text, numberic, integer, real, blob)

# excute에 sql 작성

c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, \
    username TEXT, email TEXT, \
    phone TEXT, website TEXT, regdate TEXT)")


# data 삽입하기 :하나씩 삽입하기
# ? 연산자 : tuple 형태로 변수값 입력할 때 사용
 # comma 포함되지 않으면 error 발생
# c.execute("INSERT INTO users VALUES(1, 'KD','DASDF@AGD.COM','010-0000-0000','KIN.DE.RK',?)",(nowDatetime,))
# # VALUES를 이용하여 입력할 경우 
# c.execute("INSERT INTO users(id,username,email, phone,website,regdate) VALUES (?,?,?,?,?,?)",(2,'HAY','PARK@ASD.DOC','010-1111-2222','23.COM',nowDatetime))

# Many 삽입 (/w tuple, list)

userList=( 
    (3, 'ess','DASDF@AGD.COM','010-0000-0000','KIN.DE.RK',nowDatetime),
    (4, 'kay','DASDF@AGD.CO.KR','030-0000-0000','3dN.DE.RK',nowDatetime),
    (5, 'end','DASDF@AGD.COM','040-0000-0000','sdfaN.DE.RK',nowDatetime)
)

# c.executemany("INSERT INTO users(id,username,email, phone,website,regdate)VALUES(?,?,?,?,?,?)",userList)
# 파일이나 웹크롤링을 이용하여 얻은 데이터를 한번에 DB에 밀어넣는게 효율적임 

# Table Data 삭제
# conn.execute("DELETE FROM users")
# 삭제시 삭제한 레코드수 표시
# print("user db deleted : ", conn.execute("DELETE FROM users").rowcount)

# commit, rollback, disconnect
# commit : isolation_leve= None일 경우 자동으로 입력
# conn.commit() # commit용 명령어 
# conn.rollback() # 실행 취소 

# resource 사용후에는 자동으로 해제 필요
conn.close()
