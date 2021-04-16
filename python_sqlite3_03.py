# DB 연동 /w SQLite
# table data 수정 및 삭제 

# library import
import sqlite3

# DB 생성
conn= sqlite3.connect('./path/db_test.db')
# cursor binding
c= conn.cursor()

# Data 수정하기1 : tuple 형태 활용
# c.execute("UPDATE users SET username = ? where id=?", ("text1",2))
# 수정되지 않음 : commit을 하지 않았기 때문에 db파일에 반영되지 않는다.

# Data 수정하기2 : dictionary
# c.execute("UPDATE users SET field1 =:field1 where id=:id", {"field1:"field1","id":5})

# Data 수정하기3 : formatting
# c.execute("UPDATE users SET field1 ='%s' where id='%s'" % ("field1",350)



# commit 실행 후 db browser에서 새로고침하면 반영된 결과 확인
# conn.commit() 

# Data 변경 사항 확인 
for user in c.execute("SELECT * FROM table"):
    print(user)

# field 삭제 방법1 : tuple
# c.execute("delete from table where id=?", (2,))

# field 삭제 방법2 : dictionary
# c.execute("delete from table where id=:id", {"id":5})

# field 삭제 방법3 : formatting
# c.execute("delete from table where id='%s'" % 4)
# conn.commit() 

for user in c.execute("SELECT * FROM table"):
    print(user)

# table 전체 삭제하기 
print("users db deleted : ", conn.execute("delete from table").rowcount, " rows")

conn.commit() 

# 접속해제
conn.close()
