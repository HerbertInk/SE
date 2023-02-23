# Prompt for Conditional Execution
# Range 0 <= num <= 10
num = float(input("Enter Digit: "))
if num < 5:
    print("Less")
if 5 <= num <= 7:
    print("Medium")
if 7 < num <= 10:
    print("Excellent")
print("Done")
