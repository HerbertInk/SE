try:
    code = str(input("Customer's code: "))
    while True:
        if code == 'r' or code == "R":
            print("Valid code r")
            break
        elif code == 'c' or code == "C":
            print("Valid code C")
            break
        elif code == 'i' or code == "I":
            print("Valid code I")
            break
            begin = int(input("Enter beginning meter reading:"))
            end = int(input("Enter ending meter reading:"))
            #break
            if begin < end:
                gallons = (end - begin) / 10
            else:
                gallons = ((1000000000 - begin) + end) / 10
            if code == 'r':
                bill = 5 + (gallons * 0.0005)
            elif code == 'c':
                if gallons <= 4000000:
                    bill = 1000
                else:
                    extra = gallons - 4000000
                    bill = 1000 + (extra * 0.00025)
                if code == 'i':
                    if gallons <= 4000000:
                        bill = 1000
                    elif code == "i":
                        if 4000000 < gallons <= 10000000:
                            bill = 2000
                else:
                    extra = gallons - 10000000
                    bill = 2000 + (gallons * 0.00025)
                print("Customers code:", code)
                print("Beginning meter reading", begin)
                print("Ending meter reading", end)
                print("Gallons:", gallons)
                print("Billing:", bill)
        else:
            print("Ink")
except:
    print("Invalid input")
# Done
