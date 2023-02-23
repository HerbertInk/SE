# Give a print of the nth letter in the variable ink
# Index position, value >>> str
# extraction 4rm ink >>assign to var. letter
# Int>>>[index] *float!!!*
# space is accommodated for
# zero-th--->>> nth
ink = 'herbert n'
letter = ink[3]
print(letter)
# Index is an offset from the beginning of a string
# Generating length of a str len
length = len(ink)
print(length)
# Getting last letter in the str
# The fact of making a count from zero >>> (length - 1)
# line(4)
last = ink[length - 1]
print(last)
# Else kind of extraction of the last letter
last = ink[-1]
print(last)
# Traversal through a string with a loop
index = 0
while index < len(ink):
    letter = ink[index]
    index = index + 1
    print(letter)
#    continue or break
# BREAK
print('Into the Break Statement')
index = 0
while index < len(ink):
    letter = ink[index]
    index = index + 1
    print(letter)
    break
print('imparting length')
length = 0
while length < len(ink):
    length = len(ink)
    print(length)
    break
#    pass
# CONTINUE
print("Into the continue statement")
index = 0
while index < len(ink):
    letter = ink[index]
    # + 1 lets the print begin at 1:
    index = index + 1
    print(letter)
    continue
    # print will be h
# unreachable    index = index + 1
# CONTINUE if nt  "    index = index + 1" >>>> Infinite loop
# In DESCENDING
print(" Chapter 6: Exercise 1\nInto the DESCENDING")
index = -1
while index < len(ink):
    letter = ink[index]
    index = index - 1
    print(letter)
    continue
else:
    print('Cool')
# Another to write a traversal loop is For loop
# Use of for loop??????
ink_for = 'herbert n'
char = ink_for
for char in ink_for:
    print(char)
