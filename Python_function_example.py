# 함수 정의 방법
# def 함수명(parameter):

# 예제 (다중리턴)
def func_mul(x):
    y1=x*100
    y2=x*200
    y3=x*300
    return y1,y2,y3
val1,val2,val3=func_mul(100)
print(type(val1),val2,val3)

# 예제 (다중리턴, 데이터 타입 변환)
def func_mul2(x):
    y1=x*100
    y2=x*200
    y3=x*300
    return [y1,y2,y3]
lt = func_mul2(100)
print(lt)


def args_func(*args):
    # for t in args:
    #     print(t)
    for i,v in enumerate(args): #enumerate를 사용하면 순서가 없는 Tuple에서도 순서대로 부여 가능
        print(i,v)
args_func('kim')
args_func('kim','park')
args_func('kim','park','lee')

def args_func2(*args):
    # for t in args:
    #     print(t)
    for i,v in enumerate(range(10)):
        print(i,v)
args_func2('kim')


# kwargs
def kwargs_func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

kwargs_func(name1='kim',name2='park')


# 전체 혼합
def example_mul(arg1,arg2,*args,**kwrags):
    print(arg1,arg2,args,kwrags)

example_mul(10,20)
example_mul(10,20,'park','kim',age1=24)


# 예제 : 함수에 힌트 추가
def func_mul3(x: int)-> list:
    y1=x*100
    y2=x*200
    y3=x*300
    return [y1,y2,y3]

# 예제 5 : 중첩 함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print('>>>>',num)
    print('in func')
    func_in_func(num+10000)
nested_func(10000)

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화 

# 일반적 함수 -> 변수 할당, 하나의 객체로 메모리에 할당됨
def mul_10(num:int) -> int:
    return num*10
var_func=mul_10
print(var_func)
print(type(var_func))
print(var_func(10))

lambda_mul_10=lambda num : num*10

print('>>>',lambda_mul_10(10))

def func_final(x,y,func):
    print( x* y*func(10))
func_final(10,10,lambda_mul_10)

print(func_final(10,10,lambda x : x*1000))