# python module & package
# 상대 경로
# .. : Parent Directory
# .: Current Directory

# 다양한 pkg 임포트 하여 활용

# 사용 1
# from pkg경로 import class

# 사용2  (클래스 전체 지정)
# from pkg.name import *

# 사용3 (클래스 별명 지정)
# from pkg.name import Fibonacci as fb

#  사용4 (함수)

# import pkg.function as f


# 사용 5(함수)
from pkg.calculations import div as d
print("ex5 : ", int(d(100,10)))

# 사용6 
# import pkg.prints as p
import builtins # 내장함수 Import 가능
p.prt1()
p.prt2()


# 단위 실행 (독립적으로 파일 실행)
# 패키지 내에서 파일 실행 할 때 필요
if __name__=="__main__":
    func()
    
    
