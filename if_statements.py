# a=10
# if (a>5)|(a>100):
#     print("참입니다")
# if a>5 or a>100:
#     print("참입니다")
# #비트연산이란 2진법의 숫자를 or, and, xor등으로
# #cpu내부적으로 계산하는 방식
# # and는 &과 같고, or는 |과 같고, not은 부정의 의미
# #not True는 False가 되고, not False는 True가 된다

# #대입연산자
# a=10
# #a=a+1 이렇게 표현해도 되고, a+=1 이렇게 표현도 가능
# a+=1
# print(a)
# # -=, /=, *=




# #if문의 기본 문법
# #else는 optional 요소.
# #else상단에 있는 if 또는 elif에 종속된다.
# #elif도 마찬가지로 elif상단에 if에 종속된다.

# '''
# 숫자를 입력받아서 90이하면 예각입니다.를 출력
# 90이면 직각, 91~179면 둔각, 180이면 평행
# '''
# num1=int(input("숫자를 입력해주세요"))
# if num1<90:
#     print("예각입니다.")
# elif num1==90:
#     print("직각입니다")
# elif 90<num1<180:
#     print("둔각입니다")
# elif num1==180:
#     print("평행입니다")


# # if 참조건:
# #     print("참입니다") #실행문 예제
# # else:
# #     print("거짓입니다") #실행문 예제

# # a=int(input("숫자를 입력해주세요"))
# # if a>10:
# #     print("a는 10보다 큽니다")
# # else:print("a는 10보다 작습니다.")

# # trueOrFalse=True
# # if trueOrFalse:  #if True:와 같은 의미임
# #     print("참입니다")
# # else:
# #     print("거짓입니다")

# #연습문제
# #얼마를 가지고 있습니까?를 변수에 담고, 만약 30,000이상이 있으면
# #택시를 타고 가시오를 출력, 그렇지 않으면 걸어가시오를 출력
# money=int(input("얼마를 가지고 있습니까?:"))
# if money>=30000:
#     print("택시를 타고 가시오")
# else:
#     print("걸어가시오")

# #if문 한줄로 쓰기
# #코드가 짧고 단순한 경우에 아래와 같이 한줄로 쓰는 것을 권장
# #두줄이상의 코드를 한줄로 적고 싶으면 ;으로 구분
# a=10
# if a>1: print("a는 1보다 큽니다.")

# #조건부표현식(삼항연산자):간단한 식으로 표현
# #먼저 if문의 실행문을 if문 앞으로 옮기고 :을 빼고 한줄로 변경 가능!
# # a=10
# # print("a는 10보다 큽니다") if a>10 else print("a는 10보다 작습니다")
# # #실행문을 실행하기위해 사용한다기 보다는
# # #참인경우에 어떤값, 거짓인 경우에 어떤값을 쉽게 result에 담기위해
# # result='a는 10보다 큼' if a>10 else 'a는 10보다 작음'

# # #연습문제
# # lista=[1,2,3,4,5,6,7,8,9,10]
# # numa=int(input("숫자 하나를 입력하세요:"))
# # if numa in lista:
# #     print("입력하신 숫자는 존재합니다")
# # else:
# #     print("입력하신 값은 존재하지 않습니다")


# #연습문제 2
# #항공사에서는 짐을 부칠 때 10kg이상부터 수수료를 내야한다.
# #수수료는 10의 배수 단위로 10000원씩 증가한다. 만약 10kg
# #미만이면  수수료는 없다. 사용자의 짐의 무게를 키보드로 입력 받고
# #사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성하라.
# #예시
# #짐의 무게는 얼마입니까? 21
# #짐의 무게는 21kg이며 수수료는 20000원입니다.

# weight=int(input("짐의 무게는 얼마입니까?"))
# money=(weight//10)*10000
# print("짐의 무게는 %d 이며 수수료는 %d 입니다"%(weight,money))

# # f 포맷팅
# print(f"짐의 무게는 {weight}이고 수수료는 {money}입니다")

# #연습문제
# money=int(input("돈이 얼마가 있나요?"))
# hungry=input("배가 고프신가요 yes or no로 대답해주세요")
# if money>10000 and hungry=='yes':
#     print("밥을 사먹으세요")
# else:
#     print("no")

#a와 b같은지 비교하는 연산자 is
#객체타입의 경우에는 메모리 주소를 비교하고,
#숫자,문자,bool 기본타입의 경우 값을 비교한다.
#숫자,문자,bool같은 경우에는 데이터 pool을 만들어서 재활용한다.
#그래서 값을 비교할 때 메모리 주소가 아니라, 데이터 pool에서 값을 직접 비교
a=10
b=10
if a is b:
    print("참입니다")

a=10
b=12
if a==b:
    pass  #pass시키는 것.(pass를 명시적으로 표현)
else:
    print("두 값이 다릅니다.")


