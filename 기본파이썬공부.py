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

# for ad in word:
#     if(ad != 't'):
#         print(ad)
#     else:
#         print('')

# 조건식을 작성할때는 반드시 결과값이 거짓이 나올 수 있게 만들어야 함, 그렇지 않을 경우 for문이 무한히 실행될 수 있음

user={
    "name" : '홍길동',
    "age" : 25,
    "skills" : ['python', 'git']
}
# 수정하는법
# 1. 대괄호 사용 (가장 일반적)
# print(user['name']) # 출력: 홍길동

#2. .get() 메서드 사용 (안전함)
# print(user.get("age")) # 출력: 25

# print(user['name'],"은 나이가", user['age'],"먹었습니다.")

mart = {
    "apple": 1000,
    "banana": 2000,
    "orange": 1500
}

mart["apple"] = 5000

# print(mart.keys()) # 딕셔너리의 카데고리(키)를 리스트 형태의 값으로 출력

# print(mart.values()) # 딕셔너리의 데이터를 리스트 형태의 값으로 출력

# print(mart.items()) # key와 value 를 쌍(튜플)으로 모아서 가져옴(가장 많이 씀), 데이터가 절대 변경되지 않기 때문에, 데이터 하나라도 오염되면 전부 폐기해야함.

# for fruit, price in mart.items():
#     print(f"{fruit}의 가격은 {price}원입니다.")

#     # mart.items()의 튜플값이 각각 fruit, price에 대입되며, print 내에 쉼표와 따옴표를 통해 작성하는것에 비해 프롬프트 출력에 띄어쓰기도 발생하지 않으며 손이 덜감. 맨 앞에 f를 작성한 뒤, 전체 텍스트를 큰따옴표로 일괄작성하며, 그 사이에 삽입되는 변수는 중괄호를 이용하여 표기

# for key in mart.keys():
#     print(f"mart 딕셔너리의 key값은 {key}가 있습니다.")

    # keys의 경우는 items과 다르게 하나의 카테고리 값을 리스트로 주기 때문에, 2개의 변수에 대응하지 못하는 것을 염두해야함


mart2 = {'apple': 1000, 'banana': 2500}

# print('apple' in mart2) # True 
# print('grape' in mart2) # False

my_tuple = (1, 2, 3)
another_tuple = 10, 20, 30 # 소괄호 생략 가능
# my_tuple[0] = 99 튜플은 절대 수정이 불가능

my_list = [1, 2, 3]
my_list[0] = 99 # [99, 2, 3] 으로 정상적으로 변경됨

# 리스트[] : 데이터 변경 가능(Mutable). 수정, 추가, 삭제가 마음대로 가능.
# 튜플() : 데이터 변경 불가능(Immutable). 한 번 생성되면 절대 바꿀 수 없음.

numbers = (0, 1, 2, 3, 4, 5)
print(numbers[1:4]) # (1, 2, 3) -> 인덱스 1부터 3까지 출력됨

a = (1, 2)
b = (3, 4)

print(a + b) # (1, 2, 3, 4) -> 새로운 튜플 생성
print(a * 3) # (1, 2, 1, 2, 1, 2) -> 기존 튜플을 3번 반복(복사)

# 1. 패킹
info = ('Tom', 20, 'Seoul')

# 2. 언패킹 (튜플의 개수와 변수의 개수가 같아야함)
name, age, city = info
print(name) # Tom
print(age) # 20
print(city) # Seoul

x = 10
y = 20
# 두 값을 서로 바꾸기 (튜플 언패킹 원리)
x, y = y, x
print(x) # 20
print(y) # 10

sample = (1, 2, 3, 2, 4, 2)
print(sample.count(2))
print(sample.index(3))