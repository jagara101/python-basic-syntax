#list는 변수마다 값을 할당해서 사용하기에,
#관리의 어려움이 있으므로 한 변수에 값을
#집합시켜놓은 것.

# a="김돌쇠"
# b="김갑돌"
# c="김갑순"
# print(a)
# print(b)
# print(c)

#하나의 변수로 여러개의 데이터를 관리
#list의 경우에 []대괄호를 사용하여 데이터를 집합
# lista=["a","b","c","d","e","f"]

#list안의 각각의 값에 접근할때에는 index를 사용
# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])
# print(lista[4])

#여러개의 데이터를 범위를 지정해서 가져오고 싶을때는 slicing사용
#슬라이싱의 결과값은 같은 list로 출력
#0~5번째까지 출력
# print(lista[0:5])

#0~5번째까지 출력한 결과물의 type출력
# print(type(lista[0:5]))

#문자열은 메모리 내부적으로 list와 유사한 자료구조
#문자열은 값을 추가하거나 수정할 수가 없다.
#그러나 list는 값의 추가,삭제,수정이 가능한 구조를 가지고 있다.

#연습문제2
#list_ex1=['a','b','c',[1,2,3]]이라는 리스트가 있다.
#1)변수 number에 [1,2,3]을 담아 출력하라
#2)number에 담은 값중 1과 3을 더해 4를 출력하라
# list_ex1=['a','b','c',[1,2,3]]
# number=list_ex1[3]
# print(number[0]+number[2])
# print(list_ex1[3][0]+list_ex1[3][2]) #2가지 방법으로 해결할 수 있다.

#리스트 더하기 또는 곱하기
#list 2개 선언하고 만들어서, 2개를 더해서 하나의 리스트로 만들어보자, 그리고 출력

# lista=[1,2,3]
# listb=[4,5,6]
# listc=lista+listb
# print(listc*10)

#리스트 길이 구하기: len
# print(len(lista))

#리스트 값 수정하기
# ->1개의 값만 바꿀땐 1개의 값으로 대체
# ->여러값을 바꿀땐 다른 리스트로 대체

# lista=[1,3,5,6,7,9]
# lista[1]=4
# print(lista)
# lista[2]=[5,5,5]
# print(lista)

#연습문제3 요소 개수 세기
#lista["1","2","3","4","1","1","3"]
#리스트 중 "1"이 몇 개 있는지 세보시오
# lista=["1","2","3","4","1","1","3"]
# counta=lista.count("1")
# print(counta)

#리스트 요소 삭제하기 : del
#del 리스트명[인덱스] or del 리스트명[시작:끝]
# lista=["1","2","3","4","1","1","3"]
# del lista[0:4]
# print(lista)

#리스트 요소 삭제하기: remove
#위 리스트에서 원하는 값을 삭제하라
a=[1,3,5,7,9,10]
a.remove(3)
print(a) #remove는 하나의 값만 지운다. 또한 3이 2개있다고 해서 2개다 지워지지 않는다

#모든 특정한 숫자 9값을 삭제하려면?
#del, for range 이용해보자
lista=[1,3,5,7,9,10,9]

#방법1
count=0
for a in range(0,len(lista)):
    if lista[a-count]==9:
        del lista[a-count]
        count=count+1
print(lista)


#방법2
for a in range(0,len(lista)):
    if 9 in lista:
        lista.remove(9)
    else:
        break
print(lista)

#list append: 리스트 맨 뒤로 추가
lista=[1,3,5,7]
#9,10을 append이용해서 추가해서 출력

lista.append(9)
lista.append(10)
print(lista)

#list insert: index를 지정하여 추가 가능
#list.index(2,"abc")추가 후 출력
lista.insert(2,"abc")
print(lista)

#list extend: iterable객체를 list에 추가할 때 사용
#extend는 각 요소를 꺼내어 맨 뒤에 추가
listb=[10,20,30]
lista.extend(listb)
print(lista)

#list의 정렬은 sort()함수 사용
#sort()는 오름차순 정렬

numa=[5,3,18,4,2,1]
numa.sort() #()안에 reverse=True 넣으면 내림차순 정렬
print(numa)

chlist=['brad','john','abc']
chlist.sort()
print(chlist)

#list뒤집기: reverse()
chlist.reverse()
print(chlist)

#연습문제 list 위치반환:index()
#리스트 중 "김철수"는 몇번째 문자인가?
#lista=["김돌쇠","김갑돌","김갑순","김철수"]

lista=["김돌쇠","김갑돌","김갑순","김철수"]
print(lista.index("김철수"))

#마지막 요소 끄집어내기: pop()
lista.pop()
print(lista)

#끄집어낸 요소 보이게 하는 방법
#print(lista.pop())

#문자 리스트를 문자열로 만들기
lista=["hello","world","python"]
st1=""
st2=st1.join(lista)
print(st2)
#문자열을 문자 리스트로 만들기
sta="hello world python"
sta2=sta.split()
print(sta2)


#최대값 구하기: for문만 이용, 방법1
#아래 리스트의 최대값을 정렬함수x(sort), 최대값함수 쓰지 말고 구해보라
lista=[100,20,30,5,90]


maxa=lista[0]
mina=lista[0]
for a in lista:
    if maxa<a:
        maxa=a
    if mina>a:
        mina=a
print(maxa)
print(mina)

#방법2, max함수 이용
maxA=max(lista)
minB=min(lista)
print(maxA)
print(minB)

#방법3, sort함수 이용
lista.sort()
print(lista[0])
print(lista[-1])