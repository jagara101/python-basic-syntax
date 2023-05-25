#tuple은 변경불가능한 자료형으로서,()를 통해 표현
t1=(1,2,'a','b')
print(t1)
#인덱싱,슬라이싱 둘다 리스트와 동일하게 허용
print(t1[0])

#삭제,변경 불가
# del t1[0]
# print(t1) 시도하면 오류 뜸

#튜플을 사용하는 이유는 개발자가 해당
#자료를 수정하지 못하도록 강제적으로 지정한 것

#참고사항: 리스트에 비해 메모리 효율적

#---------------------------------------------------------------

#딕셔너리 자료형은 key와 value로 이루어져있다.
#영어사전에서 단어와 뜻으로 이루어져있는것에서 유래.


#파이썬에서의 dictionary는
#다른langague의 map 또는 hashmap과 유사한 자료형
#jason이라는 자료형태와도 유사함.

#딕셔너리의 특징1
#key는 중복이 불가,
#value는 다른 key에도 존재할 수 있다.
dic1={'이름':'홍길동','나이':'25','성별':'남','성별':'여'}
print(dic1) #key값이 중복이 되면 가장 마지막 값으로 덮어짐
result={'1':80,'2':90,'3':100,'4':10}
print(result)

#딕셔너리의 기본호출 방식은 변수명[key],변수명.get(key)
print(dic1['나이'])
print(dic1.get('나이'))

#리스트는 a=[value,....] 딕셔너리는 a={key:value,...}
#튜플은 a=(value,...)
#리스트와 튜플은 a[index], 딕셔너리는 a[key]

#딕셔너리의 특징2
#key와 value로 이루어져 있다보니, 순서가 의미가 없다. index로 접근 불가
#키는 중복이 허용되지 않고, 값은 중복이 허용된다.
#key를 가지고 value를 검색할때 해시함수를 통해
#index를 찾다보니, 매우 빠른 속도를 보장(리스트보다 빠름)

dic1={'이름':'홍길동','나이':'25','몸무게':'25','성별':'남','성별':'여'}
#key:value 추가
dic1['신분']='학생'
print(dic1)

#딕셔너리에서 키를 이용한 key:value 삭제
del dic1['성별']
print(dic1)

#딕셔너리에서 key목록만을 뽑아낼때
#iterable한 형태로 data가 뽑아져 나오므로 for문 사용가능
keylist=dic1.keys()
print(keylist)

#위의 keylist에서 각각의 값을 출력해보자
for key in keylist:
    print(key)
    #key값을 출력해주는 for문안에서 value도 같이 출력하도록 해보자
    print(dic1[key])
#위의 for문을 활용해서, key가 담긴 list를 만들고, value가 담긴 list를
#만들어 각각 출력해보자
key_list=[]
value_list=[]
for k in keylist:
    key_list.append(k)
    value_list.append(dic1[k])
print(key_list)
print(value_list)

#value목록을 뽑아낼때는 .values()
# for v in dic1.values():
#     print(v)

#딕셔너리의 확장: update함수
# dic1={"a":1,"b":2,"c":3}
# dic2={"a":2,"d":4,"f":5}
# dic1.update(dic2)
# print(dic1)

#딕셔너리로 변환해서 출력해보자
#예를 들어 'a':2,'b':1,'o':2 이렇게 출력되도록 코딩해보자
lista=['a','a','b','o','o','ab','ab']
dicta={}
for i in lista:
    if i in dicta:
        dicta[i] = dicta[i] + 1
    else:
        dicta[i] = 1
print(dicta)

#방법2도 있다.(함수이용)
# lista=['a','a','b','o','o','ab','ab']
# dicta={}
# for i in lista:
#     if i not in dicta:
#         dicta[i]=lista.count(i)
# print(dicta)