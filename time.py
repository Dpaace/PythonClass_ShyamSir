# wap to find an am or pm from the time given by the user

time = int(input("Enter the time :"))
if time <= 12:
    print("It is A.M.")
elif time > 12 and time <= 24:
    print("It is P.M.")
else:
    print("Error")
