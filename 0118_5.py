# import random

# for _ in range(5):
#     n1 = random.randint(1,100)
#     print(n1, end=' ')
# print()

# for a in range(10):
#     print ('abc{}'.format(a+1),end=' ')
# print()

# for a in range(1,10):
#     for b in range(1,10):
#         if b == 9 : print('{} x {} = {:0>2}'.format(a,b,a*b))
#         else :
#             print ('{} x {} = {:0>2}'.format(a,b,a*b),end=', ')


# num1 = int(input ('시작할 수 입력: '))
# num2 = int(input ('끝나는 수 입력: '))
# num = 0
# if num1 > num2 :
#     num1, num2 = num2, num1 # 자리변환
# #     temp = num1
# #     num1 = num2
# #     num2 = temp

# for a in range(num1,num2+1):
#     if a % 2 == 0 : 
#         num += a
#         # print(num)

# print ('두 수 사이의 짝수의 합은 {}입니다.'.format(num))


print('엘리베이터 타고 내리기')
f = int(input('몇층으로 갈건가요? > '))

for a in range(1,f+1) :
    print('{}층입니다.'.format(a))

print('4층에 도착했습니다.문이 열립니다.')
