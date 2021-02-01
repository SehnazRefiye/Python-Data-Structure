def fact(num):
    if num <= 1:
        return 1
    return num*fact(num-1)

num = int(input("Please enter number: "))

while True:
    if num >= 0:
        break
    else:
        num = int(input("Enter a big number greater than zero: "))
result = fact(num)
print(result)
