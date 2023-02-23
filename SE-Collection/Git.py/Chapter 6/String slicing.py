ink = 'herbert n'
# segment of a str >> slice
print(ink[3:7])
# differences
first = ink[:4]
# prints from beginning to the 3rd
second = ink[3:]
# prints from 3rd till end of the str
print(first)
print(second)
# An empty string contains no characters and has length 0,
third = ink[4:4]
print(third)
print("Exercise 2: Given that fruit is a string, what does fruit[:] mean?")
fruit = 'banana'
exe = fruit[:]
print(exe)
print(f"this means that a str isn't segmented on print\nIt's printed as a whole.")
# concatenates a new first letter onto a slice of greeting .
greeting = 'Hello, world!'
new_greetings = 'Y' + greeting[1:]
# a space in the str also affects the program print
print(new_greetings)
print(greeting[1:])
