tp1 = (1,2,3)
print(type(tp1))
tp2 = ('f',)
print(type(tp2))
tp3 = 5,6,7
print(type(tp3))



st1 = list('hello')
print(st1)
st2 = ['hello']
print(st2)


st1 = list(['hello'])
print(st1)
st1 = list('hello454')
print(st1[::-1])

print((10,20)+(30,40,50))
print([10,20]+[30,40,50])

st1 = [1,2]
st2 = [3,4]
st3 = st1 + st2
print(st1)
print(st2)
print(st3)
print(st1)

print([1,2]*3)

a = [38,21,53,62,19]
print(len(a))
print(a[4])
print(a[len(a)-1])

a = [0,10,20,30,40,50,60,70,80,90]
print(a[1:1]) # error
print(a[2:8:3])
print(a[4:-1]) # 
print(a[5:1:-1])
print(a[:len(a)])


