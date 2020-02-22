import random

f = open('C:/Users/GREEN/Desktop/Mason/words.txt','r')
data = f.readlines()
line = random.choice(data)
word = line.strip()
f.close
print(word)

#------------------------------------
turn = 10
myguess = ''

def draw_underbar():
    for _ in word :
        print('_', end=' ')
    print('\n')
#-----------------------------------
def draw_underbar_alphabet(right):
    notfound = 0
    for ch in word :
        if ch in right :
            print(ch,end =' ')
        else :
            print('_',end=' ')
            notfound += 1
    print('\n')
    return(notfound)

#-----------------------------------
draw_underbar()

while True :
    mych = input('알파벳 하나를 추측해보세요 : ')
    if mych in word :
        myguess += mych
    else :
        turn -= 1
        print ('없는 알파벳입니다.')
        print ('{}번의 기회가 남았습니다.'.format(turn))
    
    notfound = draw_underbar_alphabet(myguess)

    if notfound == 0 :
        print('단어를 맞췄습니다. 정답은:{} 입니다.'.format(word))
        break

    if turn ==0 :
        print('더이상의 기회는 없고 정답은:{} 입니다.'.format(word))
        break
