total = 0
count = 0
while True:
    enter = float(input("Enter digit: "))
    if float(enter):
        try:
            if enter == "Done":
                break
            else:
                inp = enter
                total = total + inp
                count = count + 1
                average = total/count
        except:
            print("Invalid!!!")
    else:
        continue
print('Total:', total, 'Count:', count, 'Average:', average)
