#Write a short python function that takes a string s, representing a
#sentence and returns a copy of the string with all punctuation removed.
s = input("Please enter sentence: ")
x = ",:.;_-?*()[]'!/"
a = ""
for i in s:
    if i not in x:
       a = a + i
print(a)
