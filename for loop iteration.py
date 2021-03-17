
'''
print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)
'''

'''
print even numbers from 0 to 10
for i in range(0,10,2):
    print(i)
'''
for i in range(1,11):
    if i % 2 == 0:
        print(f'{i} Even')
    elif i % 2 != 0:
        print(f'{i} Odd')

