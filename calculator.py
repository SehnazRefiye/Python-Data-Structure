choose = None
num1 = int(input("PLease enter first number: "))
num2 = int(input("Please enter second number: "))

def multi(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def add(a, b):
    return a + b

while choose != 5:
    print("""
    1 - Multiplication
    2 - Substraction
    3 - Division
    4 - Addition
    5 - Exit
    """)

    choose = int(input("Please selected your choose: "))

    if choose == 1:
        result = multi(num1, num2)
        print('Result is: ', "{0:.5f}".format(result))

    elif choose == 2:
        result = sub(num1, num2)
        print('Result is: ', "{0:.5f}".format(result))

    elif choose == 3:
        result = div(num1, num2)
        print('Result is: ', "{0:.5f}".format(result))

    elif choose == 4:
        result = add(num1, num2)
        print('Result is: ', "{0:.5f}".format(result))

    elif choose == 5:
        print("Exited.")

    else:
        print("Your choose is wrong. ")
