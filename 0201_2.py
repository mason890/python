# print(dir(list))
# print(help(list.reverse))

#list 추가하는 방법
st = [1,2,3,4,5]

st[5:] = [6,7]
print(st)

# st.insert(5,6)
# st.insert(6,7)
# print(st)

# del st[2]
# print(st)

st[2:4]=[4]
print(st)

# st.remove(3)
# print(st)

st[5:0]=[100]
print(st)

# st.insert(5,100)
# print(st)