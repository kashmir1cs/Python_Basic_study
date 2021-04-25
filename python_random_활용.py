# 무작위 샘플링 위한 라이브러리 임포트
import random
list_random=[] # random 라이브러리를 이용하여 무작위 추출할 목록 list로  저장
n=1 # 추출 횟수 초기화 

with open('./data','r') as f: #data에서 읽어오기 (엑셀, txt, db등)
    for c in f:
        list_random.append(c.strip()) # raw data에 있는 공백 제거 하기 

while n<=5:
    random.shuffle(list_random) # 임의로 리스트 원소를 섞어줌 
    q= random.choice(list_random) # 임의로 하나를 추출 

    print()
    print("*shuffle item #{}".format(n))
    print(q) # list의 해당 원소 출력 

    n+=1 # n 증가

# 시작지점 
if __name__=="__main__" : # __main__일때만 실행하도록 변경 
    pass
