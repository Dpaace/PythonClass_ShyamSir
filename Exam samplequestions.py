'''
code to print the multiplication table of 3
n = 3
for i in range(1,11):
    prod = n * i
    print(f"{n} * {i} = {prod}")
'''

'''
0
1
2

for i in range(5):
    if i == 3:
        break
    print(i)
    
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
'''

'''
n = 5
i = 0
while i <= n:
    i += 1
    if i == 3:
        continue
    print(i)

n = 5
for i in range(n+1):
    i += 1
    if i == 3:
        continue
    print(i)
'''


'''
import random
my_list = []
for i in range(50):
    num = random.randint(1, 200)
    if num % 2 == 0:
        my_list.append(num)
'''

import random
i = 0
my_list = [ ]
while i < 50:
    num = random.randint(1,200)
    if num % 2 == 0:
        my_list.append(num)
    i += 1
print(my_list)































