# 파이썬 클래스 이해 
# Self, Class, Instance, Variable

# 클래스, 인스턴스(객체) 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간 
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재,인스턴스 생성 후 사용

# 선언

# class 클래스명:
    # 함수
    # 함수
    # 함수

# ex1
class UserInfo:
    # class 구성요소 : 속성, Method
    def __init__(self,name):
        self.name=name
    def  user_info_p(self):
        print("Name : ", self.name)


# 네임스페이스
user1=UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()

# user1과 user2는 다른 값
# id가 다른것 확인 가능 
print(id(user1))
print(id(user2))


# ex2
# self의 이해 
class SelfTest:
    def function1():
        print("function1 called!")
    def function2(self):
        print(id(self))
        print('function2 called!')
self_test=SelfTest()
# self_test.function1()
SelfTest.function1()
self_test.function2()

# id로 확인

print(id(self_test))
# SelfTest.function2() : 에러 발생
SelfTest.function2(self_test) 

# self_test, SelfTest.function2(self_test) id 동일

# ex3
# 클래스변수, 인스턴스 변수 (self 필수)
# Class "창고"생성
class WareHouse:
    # 클래스 변수 (self X)
    stock_num=0
    def __init__(self,name):
        self.name=name
        WareHouse.stock_num +=1 # 창고가 생길때마다 추가
    def __del__(self):
        WareHouse.stock_num -=1 # 삭제되면 창고숫자 1감소

user1 = WareHouse('Kim')
user2= WareHouse("Park")
user3=WareHouse("Lee")
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) 
# 클래스 네임 스페이스, 클래스 변수는 모두 공유
# (Instance에서도 호출 가능 )

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)
del user1 # 클래스 삭제 

print(user2.stock_num)
print(user3.stock_num)
