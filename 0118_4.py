# num = input('알파벳 하나를 입력하세요 => ')

# if num >= 'a' and num <= 'z' :
#     print ('소문자입니다.')
# elif num >= 'A' and num <= 'Z' :
#     print ('대문자입니다.')
# elif num >= '0' and num <= '9' :
#     print ('수자입니다.')
# else :
#     print ('알파벳도 숫자도 아닙니다.')


# import random

# num = random.randint(100,200)

# print('손님이 입장했습니다.')
# print('손님 키는 {}cm 입니다.'.format(num))
# if num >= 130 and num <= 195 :
#     print('T 익스프레스 탑승할 수 있습니다.')
# else:
#     print('T 익스프레스 탑승할 수 없습니다.')


# print('[ 비만도 진단 프로그램 ]')
# hight = float(input('키는 몇 cm 입니까? '))
# white = float(input('몸무게는 몇 kg입니까? '))

# bmi = white / ((hight/100)*(hight/100))

# if bmi >= 30 :
#     print('당신은 고도 비만입니다.',end='')
# elif bmi >= 25 and bmi < 30 :
#     print('당신은 비만입니다.',end='')
# elif bmi >= 23 and bmi < 25 :
#     print('당신은 과체중입니다.',end='')
# elif bmi >= 18.5 and bmi <23 :
#     print('당신은 정상니다.',end='')
# elif bmi < 18.5 :
#     print('당신은 저체중입니다.',end='')

# print(' (bmi = {})'.format(bmi))

# print('합격 여부 판단하기')
# num1 = int(input('국어 점수 입력 > '))
# num2 = int(input('영어 점수 입력 > '))
# num3 = int(input('수학 점수 입력 > '))
# num4 = int(input('과학 점수 입력 > '))

# avg = (num1+num2+num3+num4)/4

# if num1 < 0 or num1 > 100 or num2 < 0 or num2 > 100 or num3 < 0 or num3 > 100 or num4 < 0 or num4 > 100 :
#     print('잘못된 점수 입력 (0 ~100)')
# else :
#     if avg >= 80 :
#         print('합격')
#     else :
#         print('불합격')


print('[교통카드 잔액 출력하기]')
card = 9000
print('현재 교통카드 잔액은 {}입니다.'.format(card))

age = int(input('당신은 몇 살입니까? '))

if age >= 8 and age <= 13 :
    price = 650
elif age >= 14 and age <= 19 :
    price = 1050
elif age >= 20 :
    price = 1250
else:
    price = 0

print('현재 교통카드 잔액은 {}원입니다.'.format(card-price))