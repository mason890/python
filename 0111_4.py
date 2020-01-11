num1 = int(input('숫자 1 입력 > '))
num2 = int(input('숫자 2 입력 > '))

num3 = int(input('{} x {} = 정답입력 < '.format(num1,num2)))

if num3 == num1*num2 :
    print('정답')
elif num3 != num1*num2:
    print('오답')

