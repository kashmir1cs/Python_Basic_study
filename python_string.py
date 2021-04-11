#  문자열, 문자열연산, 슬라이싱

str1 = "I am Adult."
str2 = 'Nice Man'
str3=""
str4 = str('ace')
print(len(str1),len(str2),len(str3),len(str4))

# escape 문자열 
escape_str1="Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \tTab\t"
print(escape_str2)

# RAw String : 있는 그대로 표시 
raw_s1=r"C:\Programs\python\bin"
print(raw_s1)  
raw_s2= r"\\a\\a"
print(raw_s2)


# 멀티라인
multi= \
"""
문자열 
멀티라인
테스트
"""
print(multi)

# 문자열 연산
str_o1='*'
str_o2='abc'
str_o3="def"
str_o4 = "Niceman"
print(str_o1*100) # 문자열 반복
print(str_o2 + str_o3)
print( "ma" in str_o4) # true/ false 반환
print ( 'z' not in str_o4) # true/ false 반환

# 문자열 형 변환 
print(str(77)+"a")
print(str(10.4))

# 문자열 함수 
# www.w3schools.com 참고 
a= 'niceman'
b='orange'
# print(a.islower())
# print(b.endswith('e'))
# print(a.capitalize())
# print(list(reversed(b)))
# 문자열 slicing
print(a[0:3])
print(a[0:4])
print(a[:len(a)])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])
