'''
if statement
---------------------
syntax:
if <condition>:
    <statements>

-------------------------------------
if-else statement
---------------------
syntax:
if <condition>:
    <statements>
else:
    <statements>

--------------------------------------
elif statement
---------------------
syntax:
if <condition>:
    <statements>
elif <condition>:
    <statements>
elif <condition n>
    <statements>
.
.
.
else:
    <statements>
'''
num = int(input("Enter the week number from 1 to 7:"))
if num == 1:
    print("It is Sunday")
elif num == 2:
    print("Is is Monday")
elif num == 3:
    print("Is is Tueday")
elif num == 4:
    print("Is is Wednesday")
elif num == 5:
    print("Is is Thursday")
elif num == 6:
    print("Is is Friday")
elif num == 7:
    print("Is is Saturday")
else:
    print("Not a valid week number")


