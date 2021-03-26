num = int(input("Enter any number:"))
num_duplicate = num
sum = 0
while num > 0:
    rem = num % 10
    cube_value = rem ** 3
    sum = sum + cube_value
    num = num // 10
print(sum)
if sum == num_duplicate:
    print("It is armstrong")
else:
    print("It is not armstrong")