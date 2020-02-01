# st = [1,2,3,4,5]
# st.append(100)

# st.insert(4,100)
# print(st)
# st.insert(len(st),100)
# print(st)
# st.insert(-1,100)
# print(st)
# st.extend([100])
# print(st)


# st = [10,20,30,40,50]

# add=st.pop()

# print(st.pop(2))
# print(st)

# st.remove(40)

# if 100 in st:
#     st.remove(100)
# if 40 in st:
#     st.remove(40)
# print(st)

# st = (11,22,33,22,55)
# print(st.index(22))

# st= [10,20,30,40,50]
# st.reverse()
# print(st)

# st= [6,2,50,4,33]
# # st.sort()
# st.sort(reverse=True)
# print(st)
# print(help(list.sort))


# st= [6,2,50,4,33]

# st.clear()
# print(st)

# st.append(['mason',30])

# print(st)

# st1 = [1,2,3,4,5]
# # st2 = st1
# st2=st1.copy()
# st2[4] = 100
# print(st1,st2)
# if st2 == st1 :
#     print('동일한 리스트를 가리키고 있음')

st = [11,2,37,23,15]
for d in st : 
    print(d)
for idx, value in enumerate(st):
    print(idx,value)