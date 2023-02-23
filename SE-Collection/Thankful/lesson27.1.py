print("****First*****")
i = 0
x = 0
while i < 4:
    x += i
    i += 1

print(x)

print("****Second*****")
x = int(input("Digit 9: "))
if x > 5:
    if x < 8:
        print(x + 1)
    else:
        print(x - 1)
else:
    print(x)

print("****Lists*****")
x = [2, 4]
x += [6, 8]
print(x[2]//x[0])
# Hint
