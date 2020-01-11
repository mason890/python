"""name='Mason'
age=20
food='라멘'
print('이름은:{},나이:{},음식:{}'.format(name,age,food))

price = 100

num = input('사탕 몇 개 줄까요? ') #str
print('총 {}원입니다.'.format(int(num)*price)) #총 가격 """

# p_score = int(input ('파이썬 점수 입력 : '))
# c_score = int(input ('C언어 점수 입력 : '))
# j_score = int(input ('자바 점수 입력 : '))

# print('평균 = {}'.format((p_score+c_score+j_score)/3))

green = '오늘 점심은 뭘 먹을까?'
print(green)
# print(green[0])
# print(green[12])
# print(green[0:2])
# print(green[3:5])
# print(green[3:2+1])
# print(green[len(green)-1])

# print(green[0:13:1])
# print(green[9:12])

# print(green[-1])
# print(green[-5:])
# print(green[5:7:1])
print(green[::-1])
import random
char=random.choice(green)

print(char)

print(green.count(" "))