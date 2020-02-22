# a = int(input())
# b = int(input())

# try :
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#         print('0으로 나눌 수 없음')

st = [1,2,3,4,5]

try :
    a = st[1]+st[3]+st[5]
    print(a)
except IndexError as e:
    print(e)