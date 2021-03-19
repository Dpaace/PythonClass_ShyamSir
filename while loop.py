'''
        While loop
syntax:
initialization
while <expression>:
    <statement>
'''

'''
i = 1
while i <= 10:
    print(i)        # i -=1 i.e. i = i -1
    i += 1          # i = i + 1
'''
#
'''
import random
number = random.randint(1, 10)
num_guess = int(input("Enter the guessing number:"))
while number != num_guess:
    num_guess = int(input("OOPs! Try again"))
else:
    print("Congralutations you are right")
'''

import random
number = random.randint(1, 10)
while true:
    num_guess = int(input("Enter the guessing number:"))
    if num_guess == number:
        print("Congralutations you are right")
        break
    else:
        print("Try again")








