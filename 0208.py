# 알파벳 문자열을 인수로 넣으면, 모두 대문자로 바꾸어 반환하는 함수를 만들자.
# def aa(a) :
#     b = a.upper()
#     return b
# a = 'dd'
# s = aa(a)
# print(s)

#2개의 숫자를 매개변수로 받아서 두 수의 합과 차를 동시에 반환하는 함수를 만들자.

# def aaa(a,b) :
#     return a+b,a-b

# # r1, r2 = aaa(12,8)
# tp = aaa(10,7)
# print(tp)

#2개의 전역변수 a와 b는 각각 10, 20. 
#func 함수를 호출했을 때, 전역변수 a와 b의 값이 바뀌도록 해 보자.

# a = 10
# b = 20
# def func() :
#     global a
#     global b
#     a,b = b,a
#     print (a,b)
# func()

#한개 또는 두개의 숫자를 입력받는 func 함수를 정의하자.
# 하나의 숫자를 입력 받으면 해당 숫자에 10을 곱해서 반환하고,
# 두개의 숫자를 입력 받으면 첫번째 숫자*두번째 숫자를 반환한다.

# def func(a,b=10) :
#     return a*b

# print(func(3))
# print(func(2,10))

