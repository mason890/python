name = 'abcdefg'
st = [12,12.4,'a','tt']
for i in range(len(name)) :
    print(name[i])

for i in name :
    print(i)
print()
print(name)

for i in range(len(st)) :
    if st[i] == 'a' :
        st[i] = 'A'
    print(st[i], end=', ')
print(st)

for i in st :
    if i == 'A' :
        i = 'a'
    print(i)
print(st)