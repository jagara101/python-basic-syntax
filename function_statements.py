a=100
#특정한 input값이 있을때,
#해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자.
#그런데, 해당 연산은 매우 빈번하게 사용이 된다고 가정하자.
# result=(((a+10)*20)/10)**2
# print(result)

#복잡한 로직의 연산을 함수화 시켜서 재사용 할 수 있게 해보자.
#input값이 있어도 되고,없어도 된다
#return값이 있어도 되고,없어도 된다
def myFunc(myinput):
    calc=(((myinput+10)*20)/10)**2
    return calc
result=myFunc(20)
print(result)

#정의된 함수를 호출할때는 함수명(input)의 형태로 호출하게 된다.

#함수 직접 구현해보기
#함수명은 myPlusFunc
#함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하는 방식
#예를 들어 100을 입력하면 1+2+3...+100
def myPlusFunc(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

result=myPlusFunc(10)
print(result)

# input값(매개변수)을 2개를 받아 2값을 더한뒤,
# *2만큼 하여 return하는 함수를 만들어보자
# 그리고 해당 함수를 호출하여 호출된 결과값을 result에 담아 출력해보자

def myCall(n1,n2):
    total=(n1+n2)*2
    return total

result = myCall(10,20)
print(result)


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
            break
    return result

r1=myIndex(lista,4)
print(r1)
