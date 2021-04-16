
# sqlite db 조회
# 라이브러리 import
import sqlite3

# DB 파일 조회 실시 
# DB 파일 연결
conn= sqlite3.connect('./path')

# cursor binding
c= conn.cursor()
# data 조회 : SELECT * FROM TABLE
c.execute("SELECT * FROM table")

# 커서 위치 변경 확인
# 1개 레코드 선택
# print("One -> \n", c.fetchone())

# 지정된 레코드 선택하기
# print("Three-> \n", c.fetchmany(size=3))

# 전체 선택
# print("All-> \n", c.fetchall())

# print("All-> \n", c.fetchall()) 
# 전체를 선택하였으나 아무것도 출력되지 않았음

# 반복문과 연계1
# rows = c.fetchall()
# for row in rows:
#     print("field => ",row)

# 반복문과 연계2
# for row in c.fetchall():
#     print("field => ",row)

# 반복문과 연계3
for row in c.execute("SELECT * FROM table ORDER BY field asc"):
    print("field => ",row)

print()

# WHERE 조건 사용1 : tuple 사용
param1=(3,)
c.execute('SELECT * FROM table WHERE field=?',param1)
print('param1',c.fetchone())
print('param1',c.fetchall()) # 데이터 조회되는 없음 

# WHERE 조건 사용2 : primary key로 조회, 문자열 formatting 이용
# https://wikidocs.net/13#_16 참고하여 문자열 formatting 활용
param2=4
c.execute('SELECT * FROM table WHERE id="%s"' % param2) # comma 안들어가는것에 유의
print('param2',c.fetchone())

# WHERE 조건 사용3 : dictionary 사용
c.execute('SELECT * FROM table WHERE field=Id' ,{"Id":5}) 
print('param3',c.fetchone())


# WHERE 조건 사용4 : 복수 조건 활용
param4 = (3,5)
c.execute("SELECT * FROM table WHERE id IN(?,?)",param4)
print('param4',c.fetchall()) # Data 여러개 조회하기

# WHERE 조건 사용5 : 복수 조건 활용 문자열 formatting 이용
# https://wikidocs.net/13#_16 참고하여 문자열 formatting 활용

c.execute("SELECT * FROM table WHERE id IN('%d','%d')" % (3,4))
print('param5',c.fetchall()) # Data 여러개 조회하기


# WHERE 조건 사용6 : 복수 조건 활용. dictionary 활용

c.execute("SELECT * FROM table WHERE id=:id1 OR id=:id2",{"id1":2,"id2":5})
print('param6',c.fetchall()) # Data 여러개 조회하기

# Dump 출력 (backup)

with conn:
    with open("./path/dump.sql","w") as f :
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print("Dump complete")
# with문을 사용하면 자동으로 close 되는 장점이 있음 
