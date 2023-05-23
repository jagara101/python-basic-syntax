# # 이 #표시는 프로그래밍에서 주석이라 말한다.
# #주석은 파이썬의 인터프리터가 인식하지 못하는 기호
# # 단축키는 ctrl + /

# #아래 a=1의 의미는 a와1이 같다라는 의미가 아니라,
# # a라는 이름의 변수에 1을 담겠다는 뜻.
# a=1
# b='1'

# #print는 실행 후 결과값을 가시적으로 보여주기 위해 터미널창에 출력하는 것
# print(a)
# print(b)

# #변수명명규칙
# #변수명을 지을때는 숫자가 먼저 나와서는 안된다.
# #변수명 중간에 띄어쓰기, 특수기호등을 일반적으로 쓰지 않는다.
# #특수부호는 일반적으로 사용하지는 않지만 _언더바는 빈번히 사용한다.

# #변수 자료형 출력해보기
# print(type(a))
# print(type(b))

# c=2.1
# print(type(c))

# #자료의 형변환
# #숫자->문자, 실수->정수
# a=10
# b=20
# #결과값이 1020이 나오도록 덧셈을 하여라
# print(str(a)+str(b))

# c=2333.3333
# #c의 소수부분을 잘라라
# print(int(c))

# #문자 자료형
# #문자는 ""쌍따옴표 또는 ''홑따옴표로 표현을 한다.
# #'a'라는 문자를 변수에 저장하게 되면, 메모리상에 어떤 숫자값으로 저장될까?
# #아스키코드라는 문자와 매핑되는 테이블을 사용하여 약속된 숫자값으로 저장
# #현대에는 아스키코드의 표현범위의 한계로 인해, utf-8을 표준으로 사용
# x='a'
# print(ord(x))
# y='A'
# print(ord(y))

# #multi line으로 문자열을 표현하고 싶으면, 
# #쌍따옴표 3개를 사용하거나 홑따옴표 3개를 사용하면 된다.

# #a='''hello
# #world'''

# #이스케이프문을 활용한 줄바꿈
# #이스케이프문이란 \n또는 \t 등의 특수기호를 말한다.
# #\n:줄바꿈, \t:tap키

# a="hello\nworld"
# print(a)

# #그렇다면 python's easy라는 문구를 출력해보자
# a1="python's easy"
# print(a1)

# #역슬래시의 또다른 활용:특수문자를 있는 그대로 표현하는 역할
# #"쌍따옴표(")는 파이썬에서 문자를 의미한다"라는 문구를 출력해보세요
# print("쌍따옴표(\")는 파이썬에서 문자를 의미한다")

# #문자열 더하기,곱하기
# #a라는 변수에 python이라는 문자열을 담고, b라는 변수에는
# #is fun이라는 문자열을 담는다.
# #그리고 c라는 변수에 두 문자열을 더한 값을 넣어 c를 출력
# a='python '
# b='is fun'
# c=a+b
# print(c)

# #문자열 곱하기
# #python python is fun 이라는 문자열을 c에 담아 출력
# c=a*2+b
# print(c)

# #파이썬에서 인덱스란, 기본적으로 특정위치를 가리키는 용도로 사용.
# #인덱스의 사용방법은 원하는대상[숫자값]
# #프로그래밍에서는 대부분의 순서는 0부터 시작한다.
# #0,1,2,3,4,5...의 체계
# #문자 h를 출력하라
# a="python's fun"
# print(a[3])

# #문자열의 마지막문자를 출력해보자
# a="python's fun python's fun python's fun"
# print(a[-1])
# #문자열의 길이를 구하는 함수는 len()
# print(a[len(a)-1])

#문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)를 삽입하는 방식.
# %s:문자열, %d:정수, %f는 실수
#포맷팅을 왜 쓰는가?
#1)문자열을 직접 삽입하면 1회성으로 coding할수밖에 없지만,
#포맷팅은 변수값을 삽입할 수 있다.
#2)따옴표를 여러번 안닫아도 된다.
# language=input("좋아하는 언어를 입력하세요")  #input값은 전부 문자열로 인식
# times=input("그 언어를 몇번이나 공부하셨나요")
# a="I studied %s %d times" % (language,int(times))
# print(a)

#아래와 같이 코딩하면 따옴표로 열고 닫고를 너무 많이해서 귀찮음
# a="I studied " + language + " very hard " + str(times) +" times"
# print(a)

# #나이가 몇살이신가요?라고 해서 나이를 받고
# #몸무게가 몇킬로그램이신가요?라고 해서 weight받고
# #my age is %d, and weight is %f kg
# #위 문자열을 포맷팅을 통해 사용자의 입력값에 따라 달라지도록 만들고, 그 결과값을 출력하라.
# age=int(input("나이가 몇살이신가요?"))
# weight=float(input("몸무게가 몇킬로그램이신가요?"))
# b="my age is %d, and weight is %f kg" %(age,weight)
# print(b)

#문자열 관련 주요 함수
#count:대상 문자열에 지정한 문자가 몇개가 있는지 출력하는 함수
# a="python"
# print(a.count('o'))

#find: 대상 문자열에서 지정한 문자가 몇번째 index에 있는지 찾는 함수
#index: find와 같은 기능
# print(a.find('o'))
# print(a.index('o'))

# #없는 문자를 찾을 때는 -1 return
# print(a.find('x'))

# #번외문제
# whatyouwant=input("아무런 문자나 입력해주세요")
# search=input("찾고자 하는 문자 1개만 입력해주세요")
# result=whatyouwant.find(search)
# if result== -1:
#     print("찾고자 하는 값이 없습니다.")
# else:
#     print("요청하신 문자는 %d 번째에 있습니다." %result)

#대소문자 변경: uppper()/ lower()
# a="hello"
# print(a.upper()) #중간에 대문자 있어도 단어 전체가 대문자 처리가 됨
# b="HELLO"
# print(b.lower())

# #문자열 양쪽 공백을 없애는 함수:strip()
# a="  hello world    "
# print(a.strip())

# #문자열 대체: replace()
# a= 'i studied python'
# print(a.replace('python','java'))

# #공백을 기준으로 문자를 자르는 함수: split()
# a= 'i studied python'
# b= a.split()
# print(b)

# #split뒤에""붙이고 진행하면 공백도 데이터값으로 인식됨
# a="i   studied   python"
# b=a.split(" ")
# print(b)

# #원하는 문자열을 기준으로 자를수도 있다.
# a="i:studied:python"
# b=a.split(":")
# print(b)

# #연습문제
# #아래와 같은 2차 방정식을 파이썬 수식으로 코딩하고 y의 결과를 출력하라
# #y=2.5 * x^ +3.3 * x + 6
# #출력화면 2차 방정식 결과:22.6

# x=int(input("x값을 입력해주세요"))
# y=2.5 * pow(x,2)+3.3*x+6
# print(y)

#연습문제
#3개의 단어를 키보드로 입력 받아 각 단어의 첫글자를 추출 후 단어의 약자를 출력하라
#<조건1> 각 단어 변수(word1,word2,word3)
#<조건2>입력과 출력 구분선:문자열 연산
#<조건3>각 변수의 첫 단어만 추춯하여 변수 저장
#예시
#첫번째단어:korea, 두번째단어:baseball 세번째단어:orag
#약자:kbo

a=input("첫번째 단어를 입력하세요:")
b=input("두번째 단어를 입력하세요:")
c=input("세번째 단어를 입력하세요:")
abc=a[0]+b[0]+c[0]
print(abc)