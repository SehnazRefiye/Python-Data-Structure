num1 = float(input('-> '))

choice = input('-> ')

num2 = float(input('-> '))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

if choice == '+':
    result = add(num1, num2)
elif choice == '-':
    result = sub(num1, num2)
elif choice == '*':
    result = multi(num1, num2)
elif choice == '/':
    result = div(num1, num2)
print("""-> = 
->""", result)

