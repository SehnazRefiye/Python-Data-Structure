#Write a short python function, minmax(data), that takes a sequence
# of one or more numbers, and returns the smallest and largest numbers,
#in the form of a tuple of lenght two.
###
def minmax(a, b):
    min = b
    max = b
    for i in range(a - 1):
        b = int(input('Please enter number: '))
        if(b > max):
            max = b
        elif(b < min):
            min = b
    min_max = (min, max)
    print('Min number: ', min_max[0], ' Max number: ', min_max[1])
x = int(input('Please enter number of numbers: '))
y = int(input('Please enter number: '))
minmax(x, y)
