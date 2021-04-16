# 파이썬 외부 파일 다루기
# Excel, csv 읽기 및 쓰기
# CSV : MIME  - text/csv
# CSV는 comma외에도 다양한 방법으로 분리되어 있음

# csv 불러오기
# import csv
import csv
with open('data.csv','r') as f:
    reader=csv.reader(f)
    # Column명 넘기기
    next(reader) # 1행을 스킵함
    # csv 결과 확인
    print(reader)
    print(type(reader))

    # method 확인
    print(dir(reader))
    print()
    for c in reader:
        print(c)

print("\n")
print("\n")
print("\n")
print("\n")

print("comma외 다른 기호로 분리되어 있는 csv 파일 ")

# comma로 구분되어 있지 않는 csv 파일 읽어오기
with open('data.csv','r') as f:
    # delimeter 옵션 지정 가능
    reader=csv.reader(f,delimiter="|")

    # Column명 넘기기
    next(reader) # 1행을 스킵함
    # csv 결과 확인
    # method 확인
    print()
    for c in reader:
        print(c)


print("\n")
print("\n")
# Dictionary 형태로 변환 

with open('data.csv','r') as f:
    reader=csv.DictReader(f)

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print("---------------")


# list 생성 후 csv에 저장
w= [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

# csv 파일 쓰기
with open('./data/data.csv','w',newline="") as f: #newline 옵션 : 한줄씩 띄지않고 연속에서 읽기
    wt=csv.writer(f)
    for v in w:
        wt.writerow(v)


# for문을 사용하지 않고 한번에 쓰기
with open('./data/data.csv','w',newline="") as f:
    wt=csv.writer(f)
    wt.writerows(w)

# Excel 읽어오기 , xls, xlsx
# 주요 라이브러리 : openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주요 사용(openpyxl,xlrd이용)

import pandas as pd
# read_excel주요 옵션 
# sheetname="시트명" 또는 숫자, header=숫자, skiprow=숫자
xlsx= pd.read_excel('sample.xlsx',)

# data 확인하기
print(xlsx.head())
print("\n")
print(xlsx.tail())
print("\n")
print(xlsx.shape) #행,열 확인 


# pandas를 활용하여 엑셀/csv로 다시 쓰기

xlsx.to_excel('result.xlsx',index=False)
xlsx.to_csv('result.csv',index=False)
