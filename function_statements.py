a=100
#특정한 input값이 있을때,
#해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자.
#그런데, 해당 연산은 매우 빈번하게 사용이 된다고 가정하자.
# result=(((a+10)*20)/10)**2
# print(result)

#복잡한 로직의 연산을 함수화 시켜서 재사용 할 수 있게 해보자.
#input값이 있어도 되고,없어도 된다
#return값이 있어도 되고,없어도 된다
# def myFunc(myinput):
#     calc=(((myinput+10)*20)/10)**2
#     return calc
# result=myFunc(20)
# print(result)

#정의된 함수를 호출할때는 함수명(input)의 형태로 호출하게 된다.

#함수 직접 구현해보기
#함수명은 myPlusFunc
#함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하는 방식
#예를 들어 100을 입력하면 1+2+3...+100
# def myPlusFunc(n):
#     total=0
#     for i in range(1,n+1):
#         total+=i
#     return total

# result=myPlusFunc(10)
# print(result)

# input값(매개변수)을 2개를 받아 2값을 더한뒤,
# *2만큼 하여 return하는 함수를 만들어보자
# 그리고 해당 함수를 호출하여 호출된 결과값을 result에 담아 출력해보자

# def myCall(n1,n2):
#     total=(n1+n2)*2
#     return total

# result = myCall(10,20)
# print(result)


#list의 index함수를 쓰지 않고,
#for문 또는 while문을 통해 숫자9가 몇번째 인덱스에 있는 값인지
#알아내는 제어문을 코딩해보자

# lista=[1,4,6,9]
# print(lista.index(9))

# for i in range(len(lista)):
#     if lista[i]==9:
#         print(i)
#         break #break를 시키는 이유, 리스트에 같은 값이 있을경우 첫번째 값만 나오게 해야하기 때문에

# 위의 for문을 활용하여 myIndex라는 이름의 함수를 만들고자 한다.
# input(매개변수)값이 2개(list,찾고자 하는 값), print는 함수내에서 하지 않고 return에 값을 담는다.
lista=[1,4,6,9]
def myIndex(num1,num2):
    result=-1
    for i in range(len(num1)):
        if lista[i]==num2:
            result=i
            #break할 필요 없이, 바로 return을 해도 된다
            #return을 하면 함수 전체가 강제 취소된다.
            break
    return result

r1=myIndex(lista,4)
print(r1)


#연습문제(사용자 정의 함수)
#키보드로 반지름의 길이를 입력받고
#원의 넓이를 구하는 함수를 만들어 결과를 출력하라.
#원의 넓이 = 반지름*반지름*3.14

#[출력화면 예시]
#원의 넓이:12.56
# def circlesize(myinput):
#     a=myinput**2*3.14
#     return a
# result=circlesize(a)
# print("원의 넓이:"+str(result))


#연습문제2(입력값이 없는 함수)
#1)hello1() 이렇게만 호출했을때 "hello1 python!" 출력
#2)print(hello2())이라고 실행했을때 "hello2 python!"출력
def hello1():
    print("hello1 python!")
hello1()

def hello2():
    result="hello2 python!"
    return result
print(hello2())

#입력값의 갯수가 정해져있지 않고 multiple한 함수
def sum(*inputs):  #입력값이 몇개든 다 받겠다라는 의미, *이 all이라는 의미도 가지고있다.
    total=0
    for i in inputs:
        total +=i
    return total

totalvalue=sum(1,2,3,4,5,90)
print(totalvalue)


#2개의 이상의 리턴값이 있는 경우
def cal(a,b):   
    result1=a+b
    result2=a-b
    result3=a*b
    return result1,result2,result3

calvalue=cal(1,2)
#계산한 첫번째 결과값은 xx, 두번째 결과값은 yy, 세번째 결과값은 zz
print(f'계산한 첫번째 결과값은 {calvalue[0]}, 두번째 결과값은 {calvalue[1]},세번째 결과값은 {calvalue[2]}') #이런식으로 진행


#함수에서 default값 미리 세팅
def cal(a,b,c='plus'):
    if c== 'plus':   
        result=a+b
    elif c=='minus':
        result=a-b
    elif c=='multiply':
        result=a*b
    return result
ex=cal(1,2) #원래 하려면 여기에 'plus'문자열을 삽입해야 하나 최초 함수 만들때 c=plus라고 기본 값을 세팅할 수 있음
#ex=cal(1,2,'minus')
#ex=cal(1,2,'multiply')
print(ex)

#매개변수(input)의 순서를 안맞추고도 원하는 매개변수의 자리에
#값을 넣어 함수를 호출하는 방법
def whoareyou(name,age,gender):
    print(f"제 이름은 {name}이고, 나이는 {age}, 성별은 {gender}입니다.")
whoareyou(age=19,name='홍길동',gender='남자')


#파이썬에서 default값 세팅하는 대표적인 예시가 print함수
#print 2개를 사용해서 줄바꿈없이 hello world라고 출력이 되도록 만들어보자.
print('hello',end=' ')
print('world')


#지역변수와 전역변수
#지역변수: 함수내에서의 변수, 함수 내에서만 유효, 해당 함수 호출이 끝나면 사라진다. 스택 메모리에 쌓임
        #  객체는 힙메모리라는 곳에 쌓임
#전역변수: 함수밖에서의 변수, 함수 내에서도 인식 가능
# a=100
# def sum(a,b):
#     #함수내에서 함수밖의 전역변수를 사용하려면 global키워드 사용
#     #여기서 a의 값은 100인가 10인가?
#     #전역변수인 a=100보다, 함수내에서 선언한 a=10이 우선적으로 인식
#     result=a+b
#     return result
# result=sum(10,20)
# print(result) 
# #함수내의 result라는 변수는 함수밖에서는 인식불가
# #우리가 result 프린트 할 수 있었던 것은, 함수내에서 어떤값을return해줬기 때문.
# print(a)

lista=[10,20,30,40]
#for문마다 같은 변수를 사용하는 것은 전역변수이기는 하지만,
#재할당을해서 사용하는 것이므로 어차피 reset되서 문제되지 않는다.
for a in range(len(lista)):
    print(a)
print(a)

#이중for문을 사용할때는 문제가 될 여지가 있다.
#다중for문을 사용할때는 상위의 for문의 변수를 잃어버리게 되므로, 다른 변수를 사용해야함
# for a in range(len(lista)):
#     for b in range(len(lista)):
#         print(a)
#         print(b)


#함수내에서 전역변수에 영향을 끼치는 방법: global
#기본적으로 함수내에서 함수밖의 전역변수를 수정할 수 없다.
#그 이유는 저장되는 메모리 위치가 다르기 때문에
# result=0
# def sum(a):
#     global result
#     result+=a
#     return result
# value=sum(10)
# print(value)

#객체는 힙메모리 영역에 저장되는데, 함수내에서도 접근하여 추가/수정이 가능하다.
#스택영역에 있는 지역변수는 함수가 끝나면 휘발되지만 힙메모리는 휘발되지 않는다.
lista=[2,3,4]
def appendtest(input1,input2):
    input1.append(input2)

appendtest(lista,5) #여기서는 값을 가져오는게 아니라 lista의 주소를 가져오는것이다.
print(lista)

#만약에 지역변수가 함수호출이 끝난뒤에도 남아있다면 어떻게 될까?
#함수에서 사용하는 지역변수가 계속 메모리에 남아있으면
#메모리 낭비뿐만 아니라 다른 함수에서 해당 변수명을 사용 할 수 없는 불편함이 있음
# def test1(result):
#     result += 10
#     return result
# def test2():
#     result += 100
#     return result
# a=test1(20)
# b=test2()

#아래의 선택정렬을 함수화시켜서 활용해보기
# lista=[93,45,21,30,20,94,66,71,45]
def mysort(lista):
    for i in range(len(lista)-1):
        #2번째 for문은 비교의 대상이 되는 index를 의미
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:   #자리 change
                # lista[i],lista[j]=lista[j],lista[i] #이렇게 해도 됨
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp

#lista에 listb를 담으면, 객체의 주소가 복사가 되게 된다.
#그래서 listb가 lista와 동일한 주소, 동일한 데이터를 갖게 된다.
lista=[5,1,2]
listb=lista
#주소 출력하는 함수: id
#print(id(lista))

#lista와 값은 갖되, 동일한 메모리 주소가 아니게 할당하고 싶으면 copy함수 사용
import copy
#얕은복사 즉, 객체안의 객체의 값은 (메모리)주소로 복사가 된다.
#깊은복사는 copy.deepcopy를 사용하여 객체의 객체도 모두 value로 복사.
listb=copy.copy(lista)
print(id(listb))
print(listb)


