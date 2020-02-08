# 언패킹 *st
# def func(a,b,c):
#     return a+b+c, a*b*c
# st = [23,6,29]
# # r = func(st)
# r = func(*st)
# print(r)
# print(r[0],r[1])

# 키워드 변수 **st
# def show_info(**st):

# def func(a,b,c):
#     return ('{}+{}+{}={}'.format(a,b,c,a+b+c))
# print(func(c=3,a=1,b=2))
# dc = {'a':1,'b':2,'c':3}
# print(func(**dc))

#map

#map 객체 = map(함수, 반복가능객체)
#반복가능객체: 시퀀스 + 딕셔너리 

# def func(myst):
#     t = []
#     for i in myst:
#         t.append(pow(2,i))
#     return t
# st = list(range(1,6))
# print(st)
# print(func(st))

# def func(a):
#     return pow(2,a)
# st = [1,2,3,4,5]
# r = list(map(func,st))
# print(r)

# st = [1.2,3.4,5.6,7.8,9.0]
# r = list(map(str,st))
# print(r)

# st = [1,2,3,4,5]
# r = list(map((lambda a : pow(2,a)),st))
# print(r)


#filter객체 = filter(함수, 반복가능객체)
#반복가능 객체를 지정된 함수로 처리하여 반환값이 True인 요소만 가져오는 함수
# def func1(myst) :
#     t = []
#     for i in myst :
#         if i % 2 :
#             t.append(i)
#     return t

# st = list(range(1,6))
# r = func1(st)
# print(r)

# def func(a):
#     return a % 2
# st = [1,2,3,4,5]
# r = list(filter(func,st))
# print(r)


# def func(a):
#     if a > 80 :
#         return True
#     else : 
#         return False
# st = [77,85,89,78,90,92]
# r = list(filter(func,st))
# print(r)

# st = [77,85,89,78,90,92]
# r = list(filter((lambda a: a > 80),st))
# print(r)


# 람다 lambda
# lambda 인수: 표현식
# 한줄짜리 표현식으로 구성된 이름없는 함수(변수선언X)

# def func(a):
#     return a**2
# print(func(3))

# print(((lambda a : a**2))(2))

# def hello():
#     print('hello python')
# ((lambda : print('hello python')))()
# print(((lambda : 'hello python'))())

# f = lambda a, b : a+b
# f(10,20)

# f = lambda s : len(s)
# f('python')











#람다와 조건부 표현식

# lambda 인수: 표현식1 if 조건식 else 표현식2
# st = list(range(1,11))
# nst = list(map(lambda x: x+10 if x % 3 == 0 else x*2,st))
# print(nst)


# 람다 대신 리스트 컴프리헨션
st = list(range(1,11))
# r = list(map((lambda x : x if x % 3 else str(x)),st))
# r = list(map((lambda x : str(x) if x % 3 ==0 else x),st))
r = [x if x%3 else str(x) for x in st]
# r = [str(x) if x%3==0 else x for x in st]
print(r)

