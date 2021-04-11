# python exception

# 문법은 에러가 없으나 코드 실행 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 검증

# Syntax Error 예시

#  print('test)
# if True
#     pass
# x=> y

# NameError : 참조 변수 없음 
# 예시
# a,b=10,15
# print(c) : 변수 'c'가 없음 

# ZeroDivsionError : 0으로 나누는 에러 
# 예시 
# print(1000/0)

# IndexError : Index 범위 오류
# 예시
x= [10,20,30]
print(x[0])

# print(x[3]) : IndexError


# KeyError : dictionary
# get 메소드 활용하면 None 반환 : 안전한 방법
dic = {'name': 'Kim', 'Age' : 33, 'City':'Seoul'}
# print(dic['hobby']) Error 발생 
# get method 사용시 none 반환 
print(dic.get('hobby'))


# AttributeError : module,class 없는 property 사용
import time
print(time.time())
# print(time.month()) # 없은 method 사용 

# ValueError : No reference
x=[1,5,9]
# x.remove(10) # list에 없는 값 지정 
# x.index(10) # 10의 인덱스 값 반환 불가 : Error 발생 

# FileNotFoundErro

# f=open('test.txt','r') # 파일 없을 경우 Error 발생 


# TypeError

x=[1,2]
y=(1,2)
z='test'
# print(x+y) # 결합 불가
# print(x+z) # 연산 불가 
print(x+list(y)) # tuple -> list 형 변환

''''예외없다고 가정하에 코딩 후
    런타임 예외 발생 시 예외 처리 방안 검토
    (=처음부터 예외를 고려하진않고 추후 고려)
    ->EAFP coding style
'''

# Exception 처리 기본
# try /except 
# try : code 일단 실행
# Error Type별로 except 실행 
# except ErrorType (안적어도 무방함) 혹은 Exception
# else : error 발생하지 않을 경우 실행
# finally : 항상 실행 

# 예외 처리 방법-1

lib=["pandas","sklearn","xlwings"]

try:
    z="pandas"
    x= lib.index(z)
    print('{} was founded in lib, {} 번째 list 원소임  '.format(z,x))

except ValueError:
    print("Not found - Value Error")
else:
    print("OK! - 예외가 발생하지 않을 경우 else문 실행")
finally:
    print("예외 처리 구문 실행 완료 : finally는 무조건 실행 함")

print("-------------------------------------------------------")
# 예외 처리 방법-2
# 어떤 Error가 발생할 지 예상되지 않을 경우
try:
    z="sklearn"
    x= lib.index(z)
    print('{} was founded in lib, {} 번째 list 원소임  '.format(z,x))

except Exception :
    print("Error 발생 : except 실행")
else:
    print("OK! - 예외가 발생하지 않을 경우 else실행")
finally:
    print("예외 처리 구문 실행 완료 : finally는 무조건 실행 함")


# No exception only finally
print("-"*60)

try:
    print('Try')
finally:
    print("finally 실행")

# except는 복수 사용 가능
print("-"*60)

try:
    z="sklearn"
    x= lib.index(z)
    print('{} was founded in lib, {} 번째 list 원소임  '.format(z,x))

except ValueError :
    print("Error 발생 : except ValueError 실행")
except IndexError :
    print("Error 발생 : except IndexError 실행")
except Exception:
    print("Error 발생 : except Exception 실행")
else:
    print("OK! - 예외가 발생하지 않을 경우 else실행")
finally:
    print("예외 처리 구문 실행 완료 : finally는 무조건 실행 함")

# exception 발생 : raise
print("-"*60)

try:
    a=123
    if a=='numpy':
        print("OK")
    else:
        print("numpy와 다른 값")
        raise ValueError
except ValueError:
    print('문제발생')
except Exception as f:
    print(f)
else:
    print("OK-else문 실행")
