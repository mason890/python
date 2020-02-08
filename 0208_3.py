#Class 
#객체(object) : 물건 또는 대상 (정의할 수 있는 모든 것)
#객체를 이루는 것은 속성(값)과 기능(동작)

# a = 10
# b = int(20)
# print(type(a))
# print(type(b))

# class 클래스이름(첫문자:대) :
#     def 기능1(self) :
#         ...
#     def 기능2(self) :
#         ...

# class Student : 
#     # def study(self) :
#         # print('공부합니다.')
#     def study(self,name,age) :
#         self.name = name
#         self.age = age
#         print('공부합니다.')
#     def play(self) :
#         print('놀기도 합니다.')
# s = Student() #객체 생성
# s.play()
# s.study('ss',30)
# print(s.name, s.age)


# class AAA :
#     def abc(self) :
#         pass
#     def ddd(self,n):
#         self.name = n
#     def show(self):
#         print(self.name)
# a = AAA()
# a.ddd('mason')
# a.show()
# print(a.__dict__)

# b = AAA()
# print(b.__dict__)
# print(dir(a))
# print(id(a),id(b))


#속성저장은 __int__()를 통해서 하자
# __init__() 함수의 정체
# 객체 생성시 자동으로 호출된다
# 왜? 속성 초기화가 목적이다.
# 생성자라고 한다.

# class Student :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def study(self):
#         print('{}은 공부도 합니다.'.format(self.name))
#     def play(self):
#         print('{}은 놀기도 합니다.'.format(self.name))

# mini = Student('mason',37)
# mini.study()
# mini.play()
# print(mini.__dict__)
# print(id(mini))


#노래 한곡 표현하는 클래스 Song 정의하기
#노래 제목, 가수이름, 재생시간
#노래 play하기, 노래 정보 보여주기

# class Song :
#     def __init__(self, title, singer, playtime):
#         self.title = title
#         self.singer = singer
#         self.playtime = playtime
#     def play(self) :
#         print('노래재생합니다.')
#     def show(self) :
#         print('노래제목: {}'.format(self.title))
#         print('노래가수: {}'.format(self.singer))
#         print('노래재생시간: {}'.format(self.playtime))
# s = Song('가을 아침','IU','4분')
# s.play()
# s.show()
# print(s.__dict__)

class Friend :
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def set_phone(self,phone):
        self.phone = phone
    def show_info(self):
        print('{},{}'.format(self.name,self.phone))
    

# f = Friend('홍길동','010-111-222')
# print(f.get_name())
# print(f.get_phone())
# f.set_phone('010-333-444')
# f.show_info()

fst = []
f1 = Friend('오동백','010-222-333')
fst.append(f1)
f2 = Friend('황용식','010-444-555')
fst.append(f2)
f3 = Friend('강필구','010-666-777')
fst.append(f3)
f4 = Friend('노규태','010-888-999')
fst.append(f4)

for i in fst :
    i.show_info()


# class FriendManager :
#     fst = []
#     def add_friend(self,f):
#         self.fst.append(f)
#     def show_all(self):
#         for d in self.fst:
#             d.show_info()