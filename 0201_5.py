st3 = [[10,20],[50,25],[70,200]]
# for f,s in st3 :
#     print(f,s)

# a = []
# for i in range(3) :
#     line = []
#     for j in range(2) :
#         line.append(0)
#     a.append(line)
# print(a)

# a = []
# print([a[i][j] for i in range(3) for j in range(2)])

#어려움
# a = [[0 for j in range(2)] 
#         for i in range(3)]
# print(a)

# st1 = [[1,2],[3,4,5]]

# # st2 = st1.copy()
# import copy
# st2 = copy.deepcopy(st1)    #딥카피 하여야 한다.

# st1[0][1] *= 10
# print(st1,st2)


# a = [[[0 for k in range(2)]
#         for j in range(3)]
#             for i in range(3)]
# print (a)

a = [[i*j for i in range(1,10)]
        for j in range(1,10)]
print (a)

print(dir(str))