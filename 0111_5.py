# import random
# st = ['김밥','사탕',77,'수원역',3.14]
# ch = random.choice(st)
# print (ch)

# aa = random.randint(1,200)
# print (aa)

import random
aa = random.randint(1,6)
bb = random.randint(1,6)
print('주사위하나는 {} 이고 하나는 {} 이다.'.format(aa,bb))
if (aa+bb) % 2 == 0: print('앞으로 3칸 이동')
else: print('뒤로 1칸 이동')