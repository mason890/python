#딕셔너리 만들기

# dc1 = {'새우':700,'치즈':850,'콘':750}
# dc2 = dict({'새우':700,'치즈':850,'콘':750})
# dc3 = dict(새우=700,치즈=860,콘=750)
# dc4 = dict(['새우',700],['치즈',850],['콘',750])

# dc_emt1 = {}
# dc_emt2 = dict()


#딕셔너리 데이터 추가  / 수정
# setdefault(키)
# 없는 키인 경우: 새로운 값 추가후, 값을 반환
# setdefault(키,값)
# 있는 키인 경우: 해당 값을 반환
# update(키=값) 반환값 없음
# 없는 키인 경우 : 새로운 값 추가
# 있는 키인 경우 : 해당값으로 수정

# dc = {'새우':700,'치즈':850,'콘':750}
# dc = dict(새우=700,치즈=850,콘=750)
# # dc['치즈'] = 900
# dc.update(치즈=900)
# print(dc)

# # dc['껌'] = 300
# dc.setdefault('치즈',300)
# print(dc)

# del dc['콘']
# print(dc['콘'])
# print(dc.get('콘'))
# print(dir(dict))


# for i in dc : print(dc.get(i))
# for i in dc.keys(): print(dc.get(i))
# for i in dc.values(): print(i)
# for k,v in dc.items(): print(k,v)


#성적 계산 - 평균 출력하기
# score = {'음악':70,'미술':66,'체육':82}
# score['도덕'] = 91
# print(score)
# s = []
# for i in score.values():
#     s.append(i)

# cont = len(s)
# print (cont)
# avg = sum(s)/cont
# print('평균={:.2f}'.format(avg))


#리스트와 튜플로 딕셔너리 만들기
# fromkeys(), fromkeys(st,10)

# st = ['a','b','c']
# dc = dict.fromkeys(st)
# print(dc)

# cdc = {k:v for k,v in dc.items()}
# print(cdc)

# #딕셔너리 컴프리헨션
# dc = {'새우':700, '치즈':850,'콘':750}
# cdc = {k:v for k,v in dc.items() if v >710 and v<800}
# print(cdc)

#셋 set 집합 (값 있는지 여부 확인용)
#다양한 자료형의 데이터를 저장 타입: set
# 중복 불가능, 수정 가능함

# list/ tuple 인덱싱 & 슬라싱연산 가능 / 수정 불가능
# dict 반복 가능 / 수정 가능
# set 인덱싱 & 슬라이싱 연산 불가능 / 수정 가능

# a = {1,2,3,4,5}
# b = set('hello')
# c = set(range(5))
# e = set()  # d = {} 이건 허용안함
# s = {'hello'}
# print(b)
# print(s)

# print(dir(set))
# myset = {5,3,6,4,6}
# myset.remove(6)
# myset.remove(8)
# myset.discard(8)   if 로 값이 있는지 확인후 써야 한다. 
# myset.pop()
# myset.clear()
# del myset
# print(myset)

#검색 수정보다 값이 있다 없다로 활용, 수정시=> 지우고 새로 추가함.

#set 컴프리헨션

# a = set('hello')
# b = {i for i in 'hello'}

# c = {i for i in range(10) if i != 2 and i != 7}
# print(c) 

#합집합 
# set1|set2 
# d = set.union(a,b)

# a = {1,2,3,4}
# b = {3,4,5,6}
# c = a | b
# d = set.union(a,b)

#교집합
# c = a & b
# d = set.intersection(a,b)

# c = a-b
# d = set.difference(a,b)

# c = a^b
# d = set.symmetric_difference(a,b)
 
# print(d)
# print(d)

# 1~100 사이 숫자 중 3과 5의 공배수를 set형식으로 출력하자.
# a = 3의 공배수 set
# b = 5의 공배수 set
# print(a&b)

# c = {i for i in range(10) if i != 2 and i != 7}


a = {i for i in range(101) if i % 3 ==0}
b = {i for i in range(101) if i % 5 ==0}
print(a)
print(b)
print(a & b)


c = [i for i in range(101) if i % 3 ==0]
d = [i for i in range(101) if i % 5 ==0]
print(c)
print(d)

