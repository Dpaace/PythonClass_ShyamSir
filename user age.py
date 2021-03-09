'''
User age teller
age = int(input('Enter the users age:'))
if age > 0 and age < 15:
    print("You are a child")
elif age > 15 and age < 40:
    print('You are an adult')
elif age > 40:
    print('You are old')
elif age < 0:
    print('Not valid')
'''

salary = 20000
expense = 0.1 * salary
net_salary = salary - expense
print(f"His net salary is {net_salary}")
