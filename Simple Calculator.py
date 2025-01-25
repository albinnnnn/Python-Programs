def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "w"
    else:
        return x / y

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    c = input("Enter choice (1/2/3/4/5): ")

    if c == '5':
        print("Exiting the calculator.")
        break
    if c in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if c == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif c == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif c == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif c == '4':
            if divide(num1, num2)=="w":
                print("Division by 0 is not possible.")
            else:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please choose a valid operation.")
