class Account :
    serial_id = 20200001
    def __init__(self,name):
        self.name = name
        self.account_id = Account.serial_id
        self.balance = 0
    def deposit(self,money) :
        pass
    def withdraw(self,money) :
        if self.balance >= money :
            self.balance -= money
        else :
            print('잔액부족')
    def showInfo(self):
        print('고객이름 : {}\n 통장번호 : {}\n 잔액 : {}'.format(self.name, self.account_id, self.balance))
class SilverAccount(Account) :
    def __init__(self,name) :
        super().__init__(name)
    def deposit(self, money) :
        self.balance += money*1.01
class GoldAccount(Account) :
    def __init__(self,name) :
        super().__init__(name)
    def deposit(self, money) :
        self.balance += money*1.3
class VIPAccount(Account) :
    def __init__(self,name) :
        super().__init__(name)
    def __str__(self) :
        return
    def deposit(self, money) :
        self.balance += money*1.5

#-------------------------------------------------
class Accountmanager :
    lst = [] # 클래스 변수

    @classmethod #클래스 메소드
    def add_account(cls,ac) :
        cls.lst.append(ac)            #클래스 메소드에서  클래스 변수 사용시 cls 로 불러온다.
        Account.serial_id += 1
    
    @classmethod
    def search_account(cls,acc_id) :
        print("-------------검색 결과입니다.----------")
        for data in cls.lst :
            if data.account_id == acc_id :
                data.showInfo()
                print("----------검색 끝-----------------")
                return
        print('해당 계좌번호 정보가 없습니다.')
        print("-------------검색 끝--------------")

    @classmethod
    def showAllInfo(cls):
        print("---------------------------")
        print("전체 계좌 정보 리스트입니다.")
        for data in cls.lst:
            data.showInfo()
        print("---------------------------")
def main() :
    # am = Accountmanager # 만들필요없음
    sa = SilverAccount('홍길동')
    Accountmanager.add_account(sa)
    ga = GoldAccount('ㅇㅇ')
    Accountmanager.add_account(ga)
    va = VIPAccount('세종대왕')
    Accountmanager.add_account(va)



    print(va) # 



    Accountmanager.search_account(20200005)
    Accountmanager.search_account(20200002)

    # Accountmanager.showAllInfo()

main() # main 함수를 호출해야 함.


#--------------------------------------------
# lst = []
# lst.append(SilverAccount('aa',1234))
# lst.append(GoldAccount('bb',1235))
# lst.append(VIPAccount('cc',1236))

# for data in lst :
#     data.showInfo()

