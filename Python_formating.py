# format 사용 [], {}, ()
# fornating 관련하여 참고하면 좋은 사이트 : https://dojang.io/mod/page/view.php?id=2300
# 중요함
print()
print('{} and {}'.format('You','Me'))
print('{0} and {1} and {0}'.format('You','Me'))
print ("{a} are {b}".format(a='You',b='Me'))

print("%s's favorite number is %d" % ('Eunki',7)) #%s : 문자 %d : 정수 , %f: 실수 


print("Test1 : %5d, price : %4.2f" % (776,6534.123))
print("Test1 : {0: 5d}, Price : {1:4.2f}".format(776,6534.123))
print("Test1: {a: 5d}, price: {b:4.2f}".format(a=776,b=6534.123)) 
