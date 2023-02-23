print("****Lists and functions****")
total = 0
count = 0
while True:
    num = input("Enter digit: ")
    if num == '':
        continue
    elif num == "done":
        break
    value = float(num)
    total = total + value
    count = count + 1

average = total / count
print("Count: ", count)
print("Average: ", average)

print("****Lists in-built functions****")
numlist = list()
while True:
    num2 = input("Enter digit: ")
    if num2 == '':
        continue
    elif num2 == 'done':
        break
    value = float(num2)
    numlist.append(value)
    # If prints_indent --> computation on every entry
average = sum(numlist) / len(numlist)
print("Length: ", len(numlist))
print("Average: ", average)

# Ink
