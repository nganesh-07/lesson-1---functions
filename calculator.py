def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select an operation from:")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")

operation = input("Enter your choice here:")

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))


if operation == "a":
    print(add(num1, num2))
elif operation == "b":
    print(subtract(num1, num2))
elif operation == "c":
    print(multiply(num1, num2))
elif operation == "d":
    print(divide(num1, num2))
else:
    print("input is invalid. try again")