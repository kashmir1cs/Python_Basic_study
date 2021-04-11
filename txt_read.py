# Section 09
# 파일 읽기, 쓰기
# 옵션 지정  읽기 r, 쓰기(기존 파일 삭제)w , 추가 (파일 생성 및 추가) a
# ..: 상대경로, .: 절대 경로 


# 파일 읽기
f=open("/path","r")
content=f.read()
print(content)
print(dir(f))
# close하여 리소스반환
f.close()
print("--------------------------------")
print("--------------------------------")
# with문 사용
# with문을 사용할 경우 별도의 close 선언없이 자동으로 리소스 반환하므로 편리
with open("/path/read.text","r") as f:
    c = f.read()
    print(c)
    print(list(c)) #리스트로 형변환 
    print(iter(c))

print("--------------------------------")
print("--------------------------------")

# iteration 하여 전체 Text 파일 내용 출력 가능 

with open("/path/read.text","r") as f: as f:
    for c in f:
        print(c.strip()) # 줄바꿈 삭제
print("--------------------------------")
print("--------------------------------")

with open("/path/read.text","r") as f:
    content=f.read() 
    # 한줄씩 읽어옴, 즉 커서가 이동하면서 text 파일에 써있는 값을 읽어서 
    # 화면에 출력함 
    print(">",content)
    content = f.read() #커서가 끝에 가 있음 : 더 이상 읽을 내용이 없음
    print(">",content) # ">"만 출력


print("--------------------------------")
print("--------------------------------")

#한 줄만 읽어오기 : 반복문필요 
with open("/path/read.text","r") as f:
    line=f.readline()
    
    # 한줄씩만 
    
    while line:
        print(line, end=">>")
        line= f.readline()
print("--------------------------------")
print("--------------------------------")


# readlines
# 전체 text 파일 내용을 List 형태로 반환
# \n 포함하여 리스트로 저장 
with open("/path/read.text","r") as f:
    contents=f.readlines()
    print(contents)
    for c in contents:
        print(c, end=" ***** ")

print("--------------------------------")
print("--------------------------------")

# 합계구하기
list_textfile=[] # 리스트 선언
with open("/path/read.text","r") as f:    
    for line in f:
        list_textfile.append(int(line))
    print(list_textfile) # list형태로 출력 가능 



# file writing

with open("./path/sample.txt","w") as f:
    f.write("TEXT1\n") # escape 문자는 즐바꿈을 의미

with open("./path/sample.txt","a") as f:
    f.write("TEXT2\n") # escape 문자는 즐바꿈을 의미


# random package 이용
from random import randint
with open("./path/test.txt","w") as f:
    for cnt in range(6): # 0~5
        f.write(str(randint(1,50))) 
        f.write('\n')

# list to text files
# writelines : list -> file
with open("./path/test.txt","w") as f:
    list= ['1st\n','2nd\n','3rd\n']
    f.writelines(list)

# print문 활용하여 파일 쓰기 
# log 파일 작성 등에 활용 가능 
with open("./path/test.txt","w") as f:
    print("첫번째 문장입니다.", file=f)
    print("두번째 문장입니다.", file=f)
