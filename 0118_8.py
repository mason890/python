# num = 10
# while num <= 10 :
#     print(num)
#     # num = num - 1

# num = -1
# while num < 0 or num > 100 :
#     num = int(input('점수 입력 > '))


# money = 0

# while money < 10000 :
#     save = int(input('저축 금액 > '))
#     money = money + save
#     print('현재 잔액은 {}원입니다.'.format(money))
# print('목표금액을 달성하였습니다.')

# while True :
#     save = int(input('저축 금액 > '))
#     money = money + save
#     print('현재 잔액은 {}원입니다.'.format(money))
#     if money >= 10000 :
#         break
# print('목표금액을 달성하였습니다.')

# import random

# com = random.randint(1,100)
# count = 0

# while True :
#     num = int(input('숫자를 추측해서 입력하세요 > '))
#     if com > num :
#         print('낮은 수자입니다.')
#         count += 1
#     elif com < num :
#         print('높은 수자입니다.')
#         count += 1
#     else:
#         print('정답입니다.')
#         count += 1
#         break

# print ('{}번째에 맞췄습니다.'.format(count))


# for i in range(1,1001) :
#     if i % 5 == 0 and i % 7 == 0 : print(i)

# i = 1
# while i>=1 and i<1000 :
#     if i % 5 == 0 and i % 7 == 0 : print(i)
#     i += 1

#continue
# for i in range(1,1001) :
#     if i % 5 != 0 or i % 7 != 0 :
#         continue
#     print(i)

num = 0
while True :
    if num % 10 == 3 :
        print(num)
    elif num > 73 :
        break
    num += 1