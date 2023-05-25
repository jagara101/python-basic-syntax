#set은 (수학)집합이라고 부르기도 한다.
#set의 특성은 딕셔너리와 마찬가지로, index가 없고 중복이 없다.
s1={'이름','나이','성별'}
#list의 중복을 제거하기 위해서
#list를 가지고 set으로 형변환 시키는 방식도 많이 사용함
s1=set(['이름','이름','나이','성별'])
print(len(s1)) #집합의 개수 구하는 함수: len
print(s1)
s2=set('test')
print(s2)

#index로 접근 불가
#print(s1[0])

#이 반 학생들의 혈액형 종류는 총 몇개인가?
lista=['a','a','a','b','b','o']
a1=len(set(lista))
print(a1)
print(set(lista))

#a1의 값을 하나씩 출력하려면?
for a in set(lista):
    print(a)

#합집합
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8])
s3=s1|s2  #프로그래밍에서 |는(쉬프트 + \누르면 됨) or(또는)를 의미
s3=s1.union(s2) #이런 방법도 있다.
print(s3)

#프로그래밍에서 &은 일반적으로 and(그리고)를 의미
#앰퍼샌드 라고 부른다.
s3=s1&s2
s3=s1.intersection(s2) #이런 방법도 있다.
print(s3)

#s2에서 s1을 뺀 차집합을 구해보자
# -,difference
s3=s2-s1
print(s3)
print(s2.difference(s1)) #이런 방법도 있다

#집합에서 값 추가: add
s1={1,2,3,4,5,6}
#7을 추가한 다음에 s1출력
s1.add(7)
print(s1)

#값 여러개 추가시 update함수(딕셔너리와 동일)
#s1에 s2를 update
#s1출력해보기

s1={1,2,3,4,5}
s2={5,6,7}
s1.update(s2)
print(s1)

#set값 삭제 시 remove,discard 함수 사용
s1={1,2,3,4,5}
#discard: remove와의 차이점은, 삭제할 값이
#존재하지 않아도 에러가 발생하지 않음
s1.remove(3)
s1.discard(4) #discard는 오류가 발생하지 않음
print(s1)

#boolean(불형)타입
#: in(또는 not in)뒤에 iterable한 자료형이 나온다
#a in lista, a not in lista, a in dicta

#비어있는 값들은 거짓, 값이 들어있으면 참
listA=[1,2,3]
while listA:
    print('참입니다')
    listA.pop()



