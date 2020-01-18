import random

score = 0

for i in range(10) :
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    check = int(input('{} x {} = '.format(num1,num2)))
    if check == num1*num2 :
        print('정답입니다.')
        score += 10
    else :
        print('오답입니다.')
print('당신의 점수는 {}입니다.'.format(score))
