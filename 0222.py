#예외 처리

# a = int(input())
# b = int(input())

# try :
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#         print('0으로 나눌 수 없음')
#---------------------------------------------

# st = [1,2,3,4,5]
# try :
#     a = st[1]+st[3]+st[5]
#     # a = st[1]+st[3]+st[4]
# except IndexError as e:
#     print(e)
# else :
#     print(a)
#     print('예외 안 나면 실행된다.')
# finally :
#     print('무조건 실행된다.')
#-----------------------------------------------


#if ~ else
#for ~ else : for 루프를 빠져나간 경우 else 실행
#try ~ except else : try 영역에서 예외 발생하지 않았을 때 무조건 else 실행
#finally : 무조건 실행된다.

#----------------------------------------------

# raise Exception('예외메시지')

# try :
#     age = int(input('나이 입력 :'))
#     if age<0 :
#         raise Exception('나이는 음수가 입력될 수 없다.')
# except Exception as e :
#     print(e)
# else :
#     print('나이: {}'.format(age))

#-----------------------------------------------

# def inputInfo() :
#     name = input('이름 입력 > ')
#     age = int(input('나이 입력 > '))
#     if age < 0 :
#         raise Exception('나이 음수 입력 안됨')
#     else :
#         print('{} : {}'.format(name,age))

# # inputInfo()

# try :
#     inputInfo()
# except Exception as e :
#     print(e)

#----------------------------------------------

#사용자 정의 예외
# Exception 상속받아 예외 클래스를 정의
# raise 는 객체를 생성한다.

# class AgeInputException(Exception) :
#     def __init__(self) :
#         super().__init__('나이 음수 입력 안됨')

# try :
#     name = input('이름 입력 > ')
#     age = int(input('나이 입력 > '))
#     if age < 0 :
#         raise AgeInputException #AgeInputException() 로 해도 되지만 raise 뒤에는 객체 자동생성되므로 ()를 안해도 된다. 

#     else :
#         print('{} : {}'.format(name,age))
# except Exception as e :
#     print(e)

#-------------------------------------------

# 아이디(8글자 이상)와 비밀번호(알파벳과 숫자로만 구성) 을 입력하여 회원가입한다.
# class AddNumberAlpaException(Exception) :
#     def __init__(self,id,pwd) :
#         if len(id) < 8 :
#             super().__init__('id 는 8글자 이상이여야 한다.')
#         if pw.isalnum() != True :
#             super().__init__('pw 는 알파벳과 숫자로만이여야 한다.')
# try :
#     id = input('이름 입력 > ')
#     pw = input('나이 입력 > ')
#     if len(id) < 8 or pw.isalnum() != True :
#         raise AddNumberAlpaException(id,pw)
#     else :
#         print('id:{}, pw:{}'.format(id,pw))
# except Exception as e :
#     print(e)

#------------------------------------------
#iterable
# 여러 개 요소가 들어 있고, 한번에 이 요소를 하나씩 꺼낼 수 있는 객체
# range객체, 리스트, 튜플, 문자열, 딕셔너리, set
# __iter__

# print(dir(list))

#iterator 객체
# 반복 가능한 객체가 __iter__ 함수를 호출해서 생성되는 객체
# __next__ 함수를 호출해서 차례대로 다음 값을 가져올 수 있음

# >>> ir = range(1,3).__iter__()
# >>> type(ir)
# <class 'range_iterator'>
# >>> dir(ir)
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
# >>> ir.__next__() #next(ir)
# 1
# >>> ir.__next__()
# 2
# >>> ir.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> ir.__next__() 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

#-------------------------------------------------

#for 와 iterator

# st = [1,2,3,4]
# for i in st :
#     print(i)

# st = [1,2,3,4]
# # ir = st.__iter__()
# ir = iter(st)
# while True :
#     try :
#         # i = ir.__next__()
#         i = next(ir)
#         print(i)
#     except StopIteration :
#         break

# 자동 호출되는 함수 스페셜 함수

#--------------------------------------------------
#제너레이터 함수
#iterator 객체의 한 종류
#"yield" 키워드를 포함한 함수 호출을 

# yield 포함되는 함수는 일반함수가 아니라 제너레이터 함수가 된다. 
# 이 함수는 호출에 안된다. 함수로 통해서 함수를 만들었다는 뜻

# def my_gen() :
#     n = 0
#     while n <= 10 :
#         yield n
#         n += 1
# ge = my_gen()   #함수 호출되는게 아니라 제너레이터 함수 만들어짐.
# print(ge.__next__()) # 함수 호출됨.
# print(next(ge))
# for i in ge : # 제너레이터 연속으로 이어짐. 
#     print(i)

def my_gen(stop,multiple) :
    n=1
    while n*multiple < stop :
        yield n*multiple
        n += 1
for i in my_gen(20,3):
    print(i, end=' ')

