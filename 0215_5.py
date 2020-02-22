#추상 클래스
#추상 메소드를 가진 클래스
#주로 최상위 부모클래스가 해당 
#객체를 만들수 없다.

class Animal :
    def __init__(self, name):
        self.name = name
    def sound(self):
        print('소리가 납니다.')
class Dog(Animal) :
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print('멍멍')
    def smell(self):
        print('냄새 맡는다.')
class Cat(Animal) :
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print('야웅')
    def jump(self):
        print('점프한다.')
class Cow(Animal) :
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print('음메')
    def milk(self):
        print('우유만든다.')
class Mouse(Animal) :
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print('찍찍')
    def smell(self):
        print('달린다.')

stl = []


# from abc import *
# class animal(metaclass=ABCMeta):
#     def __init__(self,name):
#         self.name = name
#     @abstractmethod
#     def sound(self):
#         pass