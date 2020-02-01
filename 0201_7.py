# def water(s,ml) :
#     print('컵')
#     print('{}물 따라서 {}ml 마신다'.format(s,ml))
#     print('30초동안 마신다')

# print('일어난다')
# water('정수기',500)
# print('씼는다')

'''
1. 반지름을 매개변수로 전달 받아서 원의 넓이를 계산해서 
모니터에 출력하는 함수
2. 밑변과 높이를 매개변수로 전달받아서 삼각형의 넓이를 
계산해서 그 결과를 반환해주는 함수
'''

# def won(a):
#     return a*a*3.14
# print(won(4))

# def sam(b,c):
#     return b*c*0.5
# print(sam(5,3))

''' 
1. 1~ 100 사이의 행운번호를 추첨해서 반환해주는 함수
2. 매개변수로 전달된 리스트의 평균을 구해서 그 결과를 
모니터에 출력해주는 함수
'''

# import random

# def hang():
#     return random.randint(1,100)
# print(hang())

# def avg(list):
#     print(sum(list)/len(list))
# avg([10,20,30])


# def one(a=1, b) : # 매개변수 첫번째는 default 로 줄수 없다.
# def one(a, b=2) :
#     print('{}야 안녕~{}'.format(b,a))
# one (10, '자두')

# def add10(a) :
#     a+=10

# def main() :
#     num = int (input())
#     add10(num)
#     print(num)
#     print(add10(num))
# main()


# def func_list(score):
#     for i in range(len(score)):
#         score[i] += 10
# def main():
#     st = [99,89,5,77,65,100]
#     func_list(st)
#     print(st)
# main()


# 반환값이 여러 개인 경우 > 튜플로 처리
# def add_sub(a,b):
#     return a+b,a-b,a*b,a/b
# def main() :
#     result = add_sub(5,8)
#     print(result[0],result[1],result[2],result[3])
# main()

#전역 변수 사용시 주의사항
# g_v = 77
# def my(a) :
#     # g_v = g_v + a
#     g_v + a
#     print(g_v)

# my(10)
# print(g_v)

#전역 변수 사용시 주의사항 > 인수로 넘기기
# g_v = 77
# def my(gv,a) :
#     gv = gv + a
#     print(gv)

# my(g_v,10)
# print(g_v)

#전역 변수 사용시 주의사항 > global 키워드
# g_v = 77
# def my(a) :
#     global g_v
#     g_v = g_v + a
#     print(g_v)

# my(10)
# print(g_v)


