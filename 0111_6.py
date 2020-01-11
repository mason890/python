print('덧셈 : +')
print('뺄셈 : -')
print('곱셈 : *')
print('나눗셈 : /')

menu = input('메뉴 선택 >>')


if menu == '+' :
    print('{} + {} = {}'.format(n1,n2,n1+n2))
elif menu == '-' :
    print('{} - {} = {}'.format(n1,n2,n1-n2))
elif menu == '*' :
    print('{} * {} = {}'.format(n1,n2,n1*n2))
elif menu == '/' :
    print('{} / {} = {}'.format(n1,n2,n1/n2))
else:
    break #print('잘못된 연산자입니다.')
    

    
n1 = int(input('숫자1 입력 : '))
n2 = int(input('숫자2 입력 : '))