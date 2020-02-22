# 정보은닉
# 

class House : 
    company = 'Korea'
    def __init__(self,y,a,p):

        self.__year = y    # _House__year 로 변경된다.
        self.__addr = a
        self.price = p    
    def showInfo(self) :
        print(House.company)
        # print(self.year, self.addr, self.price)
h = House(2019,'suwon',1000000)
h.addr = 'ddd'
h.showInfo()
print(h.__dict__)

