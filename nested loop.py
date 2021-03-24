'''
Nested loop
Syntax:
for i in range(4):          outer loop---row
    for i in range(3):      inner loop---column
        <statements>


'''

'''
for i in range(2):
    for i in range(3):
        print('2', end=' ')
    print()
'''
'''
for i in range(4):
    for j in range(i+1):
        print('*', end=' ')
    print()
'''

'''
a = 0
for i in range(5):
    for j in range(i+1):
        print(a, end=' ')
    a += 1
    print()
'''

'''
* * * * 
* * * 
* * 
*

for i in range(4,0,-1):
    for j in range(i):
        print("*", end=' ')
    print()
'''
'''
A
BB
CCC
DDDD

x= 65
for i in range(4):
    for j in range(i+1):
        print(chr(x),end=' ')
    x += 1
    print()
'''


'''
A
B C
D E F
G H I J

x= 65
for i in range(4):
    for j in range(i+1):
        print(chr(x),end=' ')
        x += 1
    print()
 '''

'''
A B C D
E F G 
H I 
J

x= 65
for i in range(4,0,-1):
    for j in range(i):
        print(chr(x),end=' ')
        x += 1
    print()
'''


































