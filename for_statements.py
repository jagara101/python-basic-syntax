#while문의 기본구조
# while 조건식: #조건식이 참인 경우 무한 반복
#     실행문

# a=10
# while a>5:
#     print("참입니다")

#조건을 체크 후 True이면 실행문을 1회 실행시키고
#다시 조건을 체크하러 돌아온다. 그리고 True이면 또 실행
#그러다가 조건이 False가 되면 while문 종료
# a=0
# while a<5:
#     print(str(a)+"반복")
#     a+=1

# 연습문제 1~1000까지만 프린트 되도록 출력
# 연습문제 1~1000까지 모두 더한 값을 출력
# a=1
# total=0
# while a<=1000:
#     total+=a
#     a=a+1
# print(total)

#while문에서 반복을 진행하다가 break를 만나면, 반복문 종료.
#1)if문을 써서 xxx한 조건에 break
# a=1
# total=0
# while True:
#     total+=a
#     if a==100:
#         break
#     a+=1   
# print(total)

#continue: 이 구문을 만나면 다시 반복문 조건으로 이동
#하단에 불필요한 로직을 수행하지 않고 다시 조건으로 이동할 수 있게 함

#아래와 같이 코딩하면 무한 반복됨
# a=0
# while a<1000:
#     print("hello")
#     continue
#     a+=1

#continue문을 활용해보자
# a=0
# total=0
# while a<1000:
#     a +=1
#     if a % 2==0:
#         continue
#     total +=a
# print(total)


#2)1~1000중에 홀수만 더해서 출력
# a=0
# total=0
# while a<1000:
#     a +=1
#     if a % 2!=0:
#         total +=a
# print(total)


#로또 번호 생성기
#랜덤의 값을 추출하는 파이썬 라이브러리 =>random
#리스트의 크기가 6개인 리스트를 만들어서 오늘의 로또번호를 만들어보자

# print(random.randint(1,45))
# import random

# a=0
# lista=[]
# while a<6:
#     b= random.randint(1,45)
#     lista.append(b)
#     a+=1
# print(lista)



#for문의 기본 구조
# for 변수 in 반복가능한 자료형(iterable)
#     실행문
# lista=[1,2,3,4,5,6,7,8,9,10]
# for a in lista:  #lista에 있는 자료가 순차적으로 a에 전부 출력이 되는 형식
#     print(a)

# listb=["abc","bcd"]
# for b in listb:
#     print(b)

# #range문법: range(x,y) x이상 y미만
# for a in range(1,101): #100까지 출력하고 싶으면 101로 기재해야함, 왜냐면 y미만이라는 공식이기 때문에
#     print(a)

#range의 의미: iterable객체
# v1=list(range(1,10))
# print(v1)

#range(x,y): x이상, y미만의 숫자를 담은 객체
#range(y): 0이상 y미만의 숫자를 담은 객체

# v1=list(range(10,20))
# #for a in 리스트를 써서 v1의 값을 모두 출력
# for a in v1:
#     print(a)

# #for a in range를 써서 v1[index]의 형태로 v1의 값을 모두 출력
# for a in range(len(v1)):
#     print(v1[a])

# #for a in 리스트 구문으로는 원본리스트 데이터를 변경 할 수 없다.
# lista=[10,20,30,40,50,60]
# lista[5]=100
# # for a in lista:
# #     a=100  #이런 방식으로는 원본의 lista의 값을 변경 할 수 없다.

# for a in range(len(lista)):
#     lista[a]=100
# print(lista)


# #리스트를 만드는 방법중에 리스트 컴프리헨션이라는 방법이 있다.
# #리스트에 0~9까지 담는 방법

# #방법1, 그냥 리스트 생성하는 방법
# lista=[0,1,2,3,4,5,6,7,8,9]

# #방법2
# lista=list(range(10))

# #방법3, 홀수인 값에 2를 곱한 값만을 list로
# lista=[]
# for a in range(10):
#     if a % 2 !=0:
#         lista.append(a*2)

# #방법4: 리스트 컴프리헨션으로 방법3을 표현
# lista= [a*2 for a in range(10) if a % 2 !=0] #장점: 간결하다
# print(lista)




#연습문제 나만의 리스트 만들기
# 리스트의 크기를 키보드로 입력받아 그 크기만큼 임의 숫자를 리스트에 추가하고, 
# 리스트의 크기와 값 전체를 출력하라. 모든 값은 키보드로 입력을 받고, list의 크기는 
# len() 함수를 통해 구하라. 단, 리스트의 크기는 10 이하로 입력하라.

# [출력화면 예시]
# 리스트의 크기를 정하세요!30
# 리스트의 크기를 10 이하로 다시 할당하세요!9
# 리스트에 값을 할당해 보세요! 1
# 리스트에 값을 할당해 보세요! 2
# …………………………………
# 리스트에 값을 할당해 보세요! 9
# 크기9의 리스트 ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 가 할당 되었어요

# size=int(input("리스트의 사이즈를 입력해주세요"))
# a=0
# lista=[]
# while a < size:
#     value=input("리스트의 값을 입력해주세요")
#     lista.append(value)
#     a+=1
# print("크기", size , "의 리스트", lista, "가 할당 되었어요")


#한 반에 수학점수가 60점이 넘으면 합격, 60점 미만이면 불합격
lista=[90,25,67,45,80]
#위 list가 학생의 번호 순서대로 있을때, 아래와 같이 출력하도록 코딩하여라.
#1번 학생은 합격입니다. 2번 학생을 불합격입니다, ...

#방법1
# num=1
# for i in lista:
#     if i>=60:
#         print("%d 번 학생은 합격입니다" %num)
#     else:
#         print("%d 번 학생은 불합격입니다." %num)
#     num+=1

#방법2 for i in range로 하는 방법
# for i in range(len(lista)):
#     if lista[i]>=60:
#         print("%d 번 학생은 합격입니다" % (i+1))
#     else:
#         print("%d 번 학생은 불합격입니다." % (i+1))




#for문과 break: for문에서 break문을 반드시 써야 하는 상황
#혈액형이 a형인 고객 선착순 1명만 찾는 상황.
lista=['b','b','ab','a','b','a']
#출력결과: n번째 고객이 이벤트에 당첨되었습니다.
# for i in range(len(lista)):
#     if lista[i] =='a':
#         print(f"{i+1}번째 고객이 당첨되었습니다")
#         break

#방법2
for i in range(len(lista)):
    if lista[i] =='a':
        answer=i+1
        break
print(str(answer) +"번째 고객이 당첨되었습니다")




#for문을 이용한 구구단
#5단 결과 출력: 
# 5X1 = 5
# 5X2 = 10 ... 이렇게 나오게 하기

#정답
# for i in range(1,10):
#     print(5 ,"X", i, "=", 5*i)  #print(f"5 X {i} = {5*i}") 이런식으로도 표현 가능


#문제2) 구구단 몇단을 계산해드릴까요?
# while True이용하기
# while True:
#     num=int(input("구구단 몇단을 계산해드릴까요?:"))
#     for i in range(1,10):
#         print(num ,"X", i, "=", num*i)  



#2중 for문
#구구단을 5단~9단까지 한꺼번에 출력해보자
# for i in range(5,10):
#     for j in range(1,10):
#         print(i, "X", j, "=", i*j)

#다른 방법2
num=5
while num<10:
    for a in range(1,10):
        print(f"{num} X {a}={num*a}")
    num+=1


#문제
lista=[10,20,30,40]
#lista의[0]와[1]의 자리를 바꾸려면?
num1=lista[0]
lista[0]=lista[1]
lista[1]=num1
print(lista)

'''
lista[0]=lista[1]
lista[1]=lista[0] 이 방법으로는 안됨
''' 
#파이썬에서 지원하고 있는 문법
# lista[0],lista[1]=lista[1],lista[0] 이렇게도 표현이 가능하다.


#for문을 이용한 정렬 알고리즘
lista=[93,45,21,30,20,94,66,71,45]
#위 리스트를 어떻게 오름차순 정렬 할 것인가?
#선택정렬: 0번째 인덱스부터 가장 작은 값을 채워나가는 방법
#첫번째 for문은 채워나가야할 index를 의미,
for i in range(len(lista)-1):
    #2번째 for문은 비교의 대상이 되는 index를 의미
    for j in range(i+1,len(lista)):
        if lista[i] > lista[j]:   #자리 change
            # lista[i],lista[j]=lista[j],lista[i] #이렇게 해도 됨
            temp=lista[i]
            lista[i]=lista[j]
            lista[j]=temp
print(lista)


#버블정렬
#직접 배우자


