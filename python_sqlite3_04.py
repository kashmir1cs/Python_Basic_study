# sqlite3 
import sqlite3


# DB 생성 및 Auto commit
# DB 경로 setup
conn = sqlite3.connect("./data.db", isolation_level=None) # 
# cursor 연결
cursor=conn.cursor()
# AUTOINCREMENT를 지정하면 ID를 하나하나입력하지 않아도 자동으로 입력가능
cursor.execute("CREATE TABLE IF NOT EXISTS records(\
    id INTEGER  PRIMARY KEY AUTOINCREMENT, \
    var1 INTEGER, var2 TEXT, \
    var3 TEXT)")
