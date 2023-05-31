# 람다함수: 1)함수를 간편하게 표현하기 위한 방식 2)함수를 변수에 담기 위한 방식
# lambda 매개변수: 실행문
def add(a,b):
    return a+b
print(add(1,2))

add_lambda=lambda a,b: a+b
print(add_lambda(1,2))

#매개변수 a를 입력했을 때,a의 제곱이 출력되는 lambda함수 만들어보기
add_lambda2=lambda a: a**2
print(add_lambda2(3))

#list에 람다 함수를 담아서 사용 가능.
cal_list=[lambda a,b: a+b, lambda a,b: a-b, lambda a,b: a*b]
cal_dict={'plus':lambda a,b: a+b,  #딕셔너리도 람다 함수에 넣을 수 있음
          'minus':lambda a,b: a-b,
          'multiply':lambda a,b: a*b}
print(cal_list[0](2,3))
print(cal_dict['plus'](2,3))

#lambda로 입력한 매개변수가 짝수이면 True, 홀수이면 False
oddornot=lambda x: True if x%2==0 else False

#map함수:특정함수와 반복가능한 자료형을 입력받아, 특정함수가 수행한 결과값을
#return하는 함수
#사용예시: map(함수,리시트(또는 튜플 등등))
def two_times(x):
    return x*2
lst=list(map(two_times,[1,2,3,4]))
print(lst)

#map함수와 lambda함수를 사용해서 입력한 list의 제곱값을
#담은 iist를 출력해보도록 하자.
lst=list(map(lambda x:x**2,[1,2,3,4]))
print(lst)

# map의 역할은 대상이 되는 리스트를 가지고, 
# 함수를 적용하여 새로운 리스트를 만들어내는 것
# filter의 역할은 대상이 되는 리스트에서 
# 함수를 적용하여 참/거짓 조건으로 값을 걸러내는 것
def trueornot(x):
    if x>0:
        return True
    else:
        return False
lst=list(filter(trueornot, [-1,0,3,-2,5]))
print(lst)

#위 로직을 lambda를 써서 바꿔보자(조건부표현식(삼항연산자) 이용)
lst=list(filter(lambda x: True if x>0 else False, [-1,0,3,-2,5])) #filter자리에 map을 쓰면 True,False로 표현됨
print(lst)

#함수형 프로그래밍을 사용하여, 주어진 list에서 홀수만 추출하도록 하여라
lista=[4,7,1,9,2,8]
lst2=list(filter(lambda x: True if x%2!=0 else False, lista))
print(lst2)

#sum:주어진 자료들의 총 합
print(sum([1,2,3]))
#아래 코드의 총합을 구해보라
lst2=sum(list(filter(lambda x: True if x%2!=0 else False, lista)))
print(lst2)

#문자를 아스키코드로 변환: ord()
print(ord('a'))
#숫자 107이 의미하는 아스키코드상의 문자는 뭘까?:chr()
print(chr(107))
#예를 들어 문자열이 주어질때 숫자를 제외하고 문자값만 새로운 문자열로 만들어보아라
str1='123asdf512kjlk'
print(ord('z')) #소문자 a~z:97~122
print(ord('Z')) #대문자 A~Z:65~90
new_str=''
for a in str1:
    if (122>=ord(a)>=97) or (65>=ord(a)>=90):
        new_str +=a
print(new_str)

#절대값 구하기: abs()
print(abs(-3))
#map을 사용해서 주어진 리스트를 절대값으로 변환한 리스트를 출력해보자
lista=[1,-5,3,8,-9]
print(list(map(abs,lista)))

#재귀함수
#factorial 예제: 10!: 10X9X...1
#변수 n을 넣었을때 n!가 나오도록 함수를 만들어보자
def factorial(n):
    total=1
    for i in range(1,n+1):
        total*=i
    return total
result=factorial(4)
print(result)

#재귀함수를 통한 factorial 예제
#재귀함수란 함수내에서 함수자기자신을 호출하는 함수.
#재귀함수에서는 반드시 재귀함수를 종료시키는 조건이 들어가야한다.
def test(n):
    if n==1:
        return 1
    return n*test(n-1)
result=test(10)
print(result)

#재귀함수를 반드시 써야만 하는 상황
#반복의 횟수를 알 수 없을때

#연습문제
#다섯개의 숫자중에 2개씩 숫자를 추출하는 경우의 수를 구하고자 한다.
#2개씩 숫자를 추출하여 list에 담아 마지막에 모든 리스트를 출력하도록 하여라
#예시) [[10,30],[20,10],...]


# def recur(lista,total_list,temp_list,n,m):
#     if m==0:
#         total_list.append(temp_list[:])
#         return 
#     for a in range(n,len(lista)):
#         temp_list.append(lista[a])
#         recur(lista,total_list,temp_list,a+1,m-1)
#         temp_list.pop()
            

# input1=[10,20,30,40,50]
# total_list=[]
# input2=3
# recur(input1,total_list,[],0,input2)
# print(total_list)



