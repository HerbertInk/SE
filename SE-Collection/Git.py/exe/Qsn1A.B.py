# score = input("enter score:")
try:
    score = float(input("Enter score:"))
    if score > 100.0:
        print("Bad score")
    if 80.0 <= score <= 100.0:
        print("A")
    if 70.0 <= score < 80.0:
        print("B")
    if 60 <= score < 70.0:
        print("C")


except:
    print("Invalid input")
