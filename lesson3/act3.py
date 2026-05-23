
num = int(input("Enter a number: "))


if num > 100:
    print("The number is greater than 100.")
else:
    print("The number is 100 or less.")

status = "even" if num % 2 == 0 else "odd"
print(f"The number is {status}.")

