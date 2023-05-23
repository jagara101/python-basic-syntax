# a=3
# b=4
# #덧셈:+, 빼기:-, 곱하기:*, 나누기:/, 몫://, 나머지:%
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)

# #제곱, 제곱근
# #2의10 제곱을 출력하라
# print(2**10)
# print(pow(2,10))
# import math
# print(math.pow(2,10))
# #1024의 제곱근을 구하라
# #제곱근은 math라는 라이브러리를 import해줘야한다.
# import math
# print(math.sqrt(1024))

# #문자열의 슬라이싱
# #슬라이싱이란 문자열을 잘라내는 것을 의미
# #대상변수[x:y]: x이상 y미만의
# #index를 가진 문자열을 잘라낸다.
# a="python is fun"
# #python만 잘라내서 b에 담아 출력해주세요
# b=a[0:6]
# print(b)
# #x,y 자리에 값이 없으면 처음부터 또는 끝까지를 의미
# #6번째 문자부터 끝까지 잘라내서 변수 b에 담아 출력
# b=a[6:]
# print(b)

# # #a[x:y:z] 여기에서 z는 z-1개씩 건너뛰고,
# # #2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력
# b=a[2:7:2]
# print=(b)

#연습문제
#A="20220505children's_day" 슬라이싱을 이용하여
#date라는 변수에 날짜, day라는 변수에 children's_day을
#담아서 각각 출력(print)하시오
a = "20220505children's_day"
date1 = a[:8]
day1 = a[8:]
print(date1)
print(day1)

#문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)를 삽입하는 방식.
# %s:문자열, %d:정수, %f는 실수
#포맷팅을 왜 쓰는가?
#1)문자열을 직접 삽입하면 1회성으로 coding할수밖에 없지만,
#포맷팅은 변수값을 삽입할 수 있다.
#2)따옴표를 여러번 안닫아도 된다.
language=input("좋아하는 언어를 입력하세요")  #input값은 전부 문자열로 인식
times=input("그 언어를 몇번이나 공부하셨나요")
a="I studied %s %d times" % (language,int(times))
print(a)

#아래와 같이 코딩하면 따옴표로 열고 닫고를 너무 많이해서 귀찮음
a="I studied " + language + " very hard " + str(times) +" times"
print(a)

#나이가 몇살이신가요?라고 해서 나이를 받고
#몸무게가 몇킬로그램이신가요?라고 해서 weight받고
#my age is %d, and weight is %f kg
#위 문자열을 포맷팅을 통해 사용자의 입력값에 따라 달라지도록 만들고, 그 결과값을 출력하라.
age=int(input("나이가 몇살이신가요?"))
weight=float(input("몸무게가 몇킬로그램이신가요?"))
b="my age is %d, and weight is %f kg" %(age,float(weight))
print(b)