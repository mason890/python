mylist = ['사과','떡볶이',50, 12.9,'피자']
print(mylist[2:4])
print(mylist[0][0])

copy = mylist[0:2]
print(type(copy))

print(mylist[1][1:3])

mylist[1] = '커피'
print(mylist)

mylist[2:3] = ['떡볶이','김밥']
print(mylist)

mylist[2:5] = ['김밥천국']
print(mylist)


mylist[2:6] = ['김밥천국']
print(mylist)




mylist = ['피자',10,'떡볶이',12.3]
print(mylist)
print(mylist[0][0])

mylist = [['김밥','우동'],[2000,4000],500]
print(mylist[0][0][1])


lst = [1,2,3,4,5,6]
lst2 = list()
lst3 = list(range(1,7))
print(type(lst))
print(type(lst2))
print(type(lst3))


print(list(range(3,51,2)))

print(lst3[::-1])

print(list(range(3,51,2))[::-1])

lst = [1,2,3,4,5]
print(lst)
lst[:] = [0]
print(lst)
print(type(lst))
lst[:] = []
print(lst)
print(type(lst))

