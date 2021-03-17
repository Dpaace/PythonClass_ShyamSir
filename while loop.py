'''
    factorial program
num = int(input("Enter any number:"))
product = 1
for i in range(num, 0, -1):
    product = product * i
print(f"The factorial of the given number {num} is {product}")

'''

num = int(input("Enter any number:"))
for i in range(1,11):
    product = num * i
    print(f"{num} x {i} = {product} ")


