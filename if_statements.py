#if문의 기본 문법
#else는 optional 요소.
# if 참조건:
#     print("참입니다") #실행문 예제
# else:
#     print("거짓입니다") #실행문 예제

# a=int(input("숫자를 입력해주세요"))
# if a>10:
#     print("a는 10보다 큽니다")
# else:print("a는 10보다 작습니다.")

# trueOrFalse=True
# if trueOrFalse:  #if True:와 같은 의미임
#     print("참입니다")
# else:
#     print("거짓입니다")

#연습문제
#얼마를 가지고 있습니까?를 변수에 담고, 만약 30,000이상이 있으면
#택시를 타고 가시오를 출력, 그렇지 않으면 걸어가시오를 출력
money=int(input("얼마를 가지고 있습니까?:"))
if money>=30000:
    print("택시를 타고 가시오")
else:
    print("걸어가시오")

#for문의 기본 구조
# for 변수 in 반복가능한 자료형(iterable)
#     실행문
lista=[1,2,3,4,5,6,7,8,9,10]
for a in lista:  #lista에 있는 자료가 순차적으로 a에 전부 출력이 되는 형식
    print(a)

listb=["abc","bcd"]
for b in listb:
    print(b)

#range문법: range(x,y) x이상 y미만
for a in range(1,101): #100까지 출력하고 싶으면 101로 기재해야함, 왜냐면 y미만이라는 공식이기 때문에
    print(a)

n=7
answer = 0

answer=n//7+1
print(answer)