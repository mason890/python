
# num = int(input('정수를 입력하세요 > '))
# if num == 0 :
#     print ('{}입니다.'.format(num))
# else:
#     print ('0 아닙니다.')


# num = int(input('정수를 입력하세요 > '))
# if num % 3 == 0 :
#     print ('3의 배수입니다.')
# elif num % 5 == 0 :
#     print ('5의 배수입니다.')
# elif num % 7 == 0 :
#     print ('7의 배수입니다.')
# else:
#     print ('그 외의 수입니다.')

import random
scores = [95.8, 80.2, 67.3, 45.2, 79.2]
score = random.choice(scores)

print('당신의 점수는 {}입니다.'.format(score), end='')

if score >= 90 : print(' 또한 A학점입니다.')
elif score >= 80 : print(' 또한 B학점입니다.')
elif score >= 70 : print(' 또한 C학점입니다.')
elif score >= 60 : print(' 또한 D학점입니다.')
else : print(' 또한 F학점입니다.')