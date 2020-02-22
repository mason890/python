import matplotlib.pyplot as plt

file = open ('/Users/masonpiao/Document/study/python/data.txt','r')
data = file.readlines()
file.close()

list = []
for n in data:
    # print(n.rstrip())
    list.append((n.rstrip()).split(','))
# print(list[16][0])

i = 0
for i in range(len(list[i])):
    if list[i][0]=='3':
        print(list[i])

