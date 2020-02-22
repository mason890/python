# 객체 변수 (instance 변수 )/ 클래스 변수 (static 변수)
# 객체 메소드 / 클래스 메소드 / static 메소드

class House :
    company = 'Korea' # 클래스 변수
    def __init__(self, y, a, p) :
        self.year = y
        self.addr = a
        self.price = p
    def showInfo(self) :
        print(House.company) # 될수록 클래스 적는다.
        #print(self.company) #함수안에 없으면 클래스 안에서 찾는다. 
        print(self.year, self.addr, self.price)
        # self 안 적으면 함수안에서 찾고 없으면 클래스가 아닌 전역에서 찾는다. 

h = House('2019','망포','10억')
h.showInfo()
print(h.__dict__)   # __dict__ 로 확인 가능한다. 
print(House.__dict__)
h.company = 'KOREA Factory'
h.showInfo()
print(h.__dict__)
print(House.__dict__)
House.company = 'KOREA Factory2' # 클래스 변수 이므로 클래스로 접근해야 수정이 가능함.
h.showInfo()
print(h.__dict__)
print(House.__dict__)

