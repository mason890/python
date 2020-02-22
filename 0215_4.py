# 클래스 상속
# 기존 클래스를 이용하여 사로운 클래스를 만들때 사용함 (재활용)
# 슈퍼(부모)클래스 / 서브(자식)클래스
# IS-A 관계

class Person : 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sleep(self) :
        print('잠을 잡니다.')
    def showInfo(self) :
        print(self.name,self.age)
class Student(Person) : # 상속
    
    def __init__(self,name,age,grade):   # 생성자인데. 객체생성할때 생성됨
        # super() 을 이용해서 부모 init변수를 가져와야 호출이 된다. 
        super().__init__(name,age)      
        self.grade = grade
    def study(self) :
        print('공부합니다.')
    def showInfo(self) :
        print(self.name,self.age,self.grade)

myst = []    
s = Student('mason',30,'중2')
s.study()
s.sleep()
s.showInfo()
print(dir(s))
print(s.__dict__)
myst.append(s)

p = Person('세종',49)
myst.append(p)

for data in myst :
    data.showInfo() 




