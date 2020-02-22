# 객체 메소드 / 
# static 메소드(클래스 이름으로 호출가능한 메소드)
# 클래스 메소드 (클래스 변수에 대해 동작하는 메소드)

class House :
    company = 'Korea' # 클래스 변수
    def __init__(self, y, a, p) :
        self.year = y
        self.addr = a
        self.price = p
    
    @staticmethod   # static 메소드. self 가 없다. '데코레이터'
    def printCompany() :
        print(House.company)
    
    @classmethod
    def printCC(cls) :
        cls.company = 'KK'  # cls 로 불러야 한다. 
        print(House.company)

    def showInfo(self) :
        print(House.company) # 될수록 클래스 적는다.
        #print(self.company) #함수안에 없으면 클래스 안에서 찾는다. 
        print(self.year, self.addr, self.price)
        # self 안 적으면 함수안에서 찾고 없으면 클래스가 아닌 전역에서 찾는다. 
House.printCompany()

h1 = House(200, 'suwon', 100000)
h1.printCompany()


House.printCC()