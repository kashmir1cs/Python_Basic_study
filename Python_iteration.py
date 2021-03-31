# 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print(q1.get('가을'))
print(''.join( q1[s] for s in q1 if s=='가을') ,end=' ')


# 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
hasApple= ['사과다!' for key,val in q2.items() if key=='사과' or val =='사과']

# 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
print(''.join(str(n) for n in range(1,100,2)))
q6=[x for x in range(1,101) if x % 2 !=0]
print('---------------------------------')
print(q6)
print('---------------------------------')

# 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
print([s for s in q4 if len(s)>=5],end=' ')
# 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for v in q5:
    if v.isupper():
        continue
    else:
        print(v,end=' ')
print([s for s in q5 if s.islower()],end=' ')