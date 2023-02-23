# Conditional steps
print("Hello, World!")
print('Conditional Execution')
while True:
    x = input("Enter Your Digit:\n")
    if x.isdigit() and 1 <= float(x) <= 20:
        print("Within Range")
        break
    else:
        print("Invalid Input")
        # break
exit()
