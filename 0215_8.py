#숫자 야구 게임
#컴퓨터가 숫자 3개 만들기
#무한 반복: 3개 숫자 추측하기
# 숫자 서로 비교하여 strike 와 ball 판정하기
# strike 가 3개이면, 반복문 빠져 나오기

import random

com = []

def make_com_number():
    while True:
        num = random.randint(0,9)
        if num not in com:
            com.append(num)
        if len(com) == 3 :
            break

make_com_number()
print(com)

me = []
def guess_number() :
    me.clear()
    for _ in range(3) :
        num = int(input('0~9사이 숫자 하나 입력: '))
        me.append(num)
    print(me)
    

def print_strike_ball() :
    s = 0
    b = 0
    for c in range(3):
        if com[c] == me[c] : s = s +1
    if com[0] == me[1] or com[0]==me[2]: b = b+1
    if com[1] == me[0] or com[1]==me[2]: b = b+1
    if com[2] == me[0] or com[2]==me[1]: b = b+1
    print('{}strike, {}ball'.format(s,b))
    return s
make_com_number()
while True:
    guess_number()
    strike = print_strike_ball()
    if strike ==3 :
        break
print('정답입니다.')