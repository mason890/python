# st4 = [d for d in range(1,7)]
# print(st4)

# st1 = [1,2,3,4,5]
# # st2 = []
# # for d in st1 :
# #     st2.append(d*3)

# st2 = [d*3 for d in st1]     #List comprehension
# print(st2)

# st = [1.2,3.4,5.6,7.8,9.9]
# # for i in range(len(st)) :
# #     st[i] = int(st[i])

# st2 = [int(st[i]) for i in range(len(st))]
# print(st2)


# st1 = [100,80,92,75,85]
# # st2 = []
# # for d in st1 :
# #     if d > 80 :
# #         st2.append(d)

# st2 = [d for d in st1 if d>80 and d<90]

# print(st2)


# st1 = ['a','b','c']
# st2 = [1,2,3,4,5]
# # st3 = []
# # for f in st1 :
# #     for s in st2 :
# #         st3.append(f+str(s))

# st3 = [f+str(s) for f in st1 for s in st2]

# print(st3)



# print([3*i for i in range(1,10)])
# print(list(3*i for i in range(1,10)))
# print(tuple(3*i for i in range(1,10)))

# print([i*j for i in range(2,10) for j in range(1,10)])


# a = ['alpha','bravo','delta','charlie','echo','foxtrot','golf','hotel','india']

# # for i in range(len(a)) :
# #     if len(a[i]) > 4 :
# #         print(a[i])

# print([a[i] for i in range(len(a)) if len(a[i]) > 4])

# 2의 거듭제곱 리스트 만들기
a = int(input())
b = int(input())
# c = []
# for i in range(a,b+1):
#     c.append(pow(2,i))
# print(c)


print([pow(2,i) for i in range(a,b+1) ])
# print(help(pow))
# print(help(range))



