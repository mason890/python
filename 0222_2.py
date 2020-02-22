# with open('C:/Users/GREEN/Desktop/Mason/words.txt','r') as fp :
#     lines = fp.readlines()
#     for line in lines :
#         print(line.strip())

# 제너레이터 이용
# def fileread_gen() :
#     with open('C:/Users/GREEN/Desktop/Mason/words.txt','r') as fp :
#         lines = fp.readlines()
#         for line in lines :
#             yield line.strip()
# for i in fileread_gen() :
#     print(i)

# 소수 출력하기

# start, stop = map(int,input('input 2 number > ').split())
# for i in range(start, stop+1) :
#     # flag = True
#     for j in range(2, i) :
#         if i % j ==0 :
#             # flag = False
#             break
#     # if flag == True :
#     else :
#         print(i, end=' ')

def p_gen(start, stop) :
    for i in range(start, stop+1) :
        for j in range(2, i) :
            if i % j ==0 :
                break
        else :
            yield i
start, stop = map(int,input('input 2 number > ').split()) # map 을 사용하여 동시에 두개 사용가능
for i in p_gen(start,stop) :
    print(i, end=' ')