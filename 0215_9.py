#파일 출력 스트림

#파이썬에서 객체 지향 pickle 모듈로 해야 한다. 

# file = open('C:/Users/GREEN/Desktop/Mason/iotest.txt','w')   # read: w -> r
# # data = file.read()
# # file.write('#파이썬 최고')
# # file.write('#나도 최고!!!')
# for c in range(1, 11, 1): 
#     d= '{}번라인입니다.\n'.format(c)
#     file.write(d)
# file.close()


# data = file.read()
# data = file.readlines() #내용 전체를 라인별로 넣은 리스트를 만들어 준다. 
# line = file.readline() #한줄만 읽어온다.

# import random
# file = open('C:/Users/GREEN/Desktop/Mason/iotest.txt','r')
# data = file.readlines()
# file.close()

# print(data[2])
# line = random.choice(data)
# print(line)


# with as : close 안해도 된다. 
# with open('C:/Users/GREEN/Desktop/Mason/iotest.txt','r') as f :
#     while True :
#         line = f.readline()
#         if line : 
#             print(line.rstrip())
#         else :
#             break


#자기소개 파일 만들기
# file = open('C:/Users/GREEN/Desktop/Mason/mystory.txt','w')
# file.write('*이름:나야나\n')
# file.write('*나이:14\n')
# file.write('*별명:나예쁨\n')
# file.close

# file = open('C:/Users/GREEN/Desktop/Mason/mystory.txt','a')
# file.write('*즐겨먹는음식:떡볶이\n')
# file.write('*취미:프로그래밍\n')
# file.close

# f = open('C:/Users/GREEN/Desktop/Mason/mystory.txt','r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close


#split
f = open('C:/Users/GREEN/Desktop/Mason/mystory.txt','r')
lines = f.readlines()
foodstr = lines[3]
foodlist = foodstr.split(':')
myfood = foodlist[1].strip()
print(myfood)
f.close

# with open('C:/Users/GREEN/Desktop/Mason/mystory.txt','r') as f :
#     while True :
#         line = f.readlines()
#         if line : 
#             print(line.rstrip())
#         else :
#             break