문자변수 = """
          띄어쓰기 하고 싶을때, 
          가독성 높이고 싶을때...
"""
num = 10 #숫자를 값으로 가지는 변수 num
count = 100

# print(num + count, 문자변수)

list = ['사과','배']

# print(type(list)) # type은 해당 데이터의 타입을 확인할 수 있는 명령어
# print("hi"*3) # 사직연산자 * 는 복사기능이 있는 명령어
a = True
b = False 
# print(type(a))
# print(type(b))
# print(10 > 5)
# python, R의 경우 true, false는 첫대문자 주의
age = 20
# print("성인" if age < 19 else "미성년자") # 삼항식 {값 if 조건식 else 값2}

num = 10
# if num > 5:
#     print('5보다 크다')
#     print('나는 if식에 귀속되어있음') # tab을 해야 if 조건식에 귀속됨
# print('나는 위의 if식과 상관없음')

score = 80

# if score >= 60:
#     print('합격')
# else:
#     print('불합격')


score = 75
# 조건을 여러가지로 하여 조건식을 만들때 이용하는 조건식이며, 수많은 조건문을 넣어도 출력되는 출력값은 조건문 중 하나뿐
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print(score,'점이라서 C')
# else:
#     print('F')

# fruits = ['사과', '바나나', '포도'] # 리스트

유치원 = {
    '해바라기' : ['유재석','박명수'],
    '장미' : [],
    '민들레' : ['배철수']
} # 딕셔너리

시각화훈련 = {
    '과목':['파이썬', '깃']
}

# 나 = {
#     "반려동물" = {
#         '고양이':['보미','겨울이'],
#         '개':['돌돌이']
#     }
# } # 파이썬에선 딕셔너리, javascript에선 오브젝트 라고 부르는 비정량 데이터

student = {
    '이름': '홍길동',
    '나이': 25
}
student['이름']

# fruits = ['사과', '바나나', '포토']

# for fruit in fruits: # 'for 임의데이터명 in 리스트명' 의 for문은 해당 리스트명을 가진 리스트의 요소를 임의데이터명에 하나씩 대입하여, pring(임의데이터명) 이 종속될 경우, 리스트의 마지막 요소까지 출력되도록 한다
#     print(fruit)

word = "python"

for ad in word:
    if(ad != 't'):
        print(ad)
    else:
        print('')

# 조건식을 작성할때는 반드시 결과값이 거짓이 나올 수 있게 만들어야 함, 그렇지 않을 경우 for문이 무한히 실행될 수 있음

