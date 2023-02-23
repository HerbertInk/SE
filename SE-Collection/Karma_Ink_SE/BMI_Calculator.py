"""BMI Calculator:
The formula (weight/height^2)
    Inputs: Weight & Height"""

"""Program exit()"""


def program_exit():
    user_exit = input("Please enter Yes or No:\nWould you like to continue: ")
    x = ['done', 'exit', 'no', 'n']
    y = ['yes', 'y']
    while True:
        if len(user_exit) > 0 and user_exit.lower() in y:
            print("Thanks!!!")
            break
        elif len(user_exit) > 0 and user_exit.lower() in x:
            exit()


def fo():
    ans = weight_exact / (height_exact * height_exact)
    print("BMI Result: ", ans)
    if ans < 18.5:
        return print("Underweight")
    elif 18.5 <= ans < 25:
        return print("Normal")
    elif 25 <= ans < 30:
        return print("Overweight")
    elif ans >= 30:
        return print("Obesity")


"""User Inputs"""

while True:
    user_entry_init = input("Enter username: ")

    if len(user_entry_init) > 0 and user_entry_init.isalpha():
        user_entry = user_entry_init

        # weight = 0    height = 0
        while True:
            weight = input("\nEnter Weight: ")
            if len(weight) > 0 and weight.isnumeric() and 0 < int(weight) < 1000:
                weight_exact = float(weight)
                break
            else:
                print("Enter valid weight")
                program_exit()
                continue
        while True:
            height = input("\nEnter Height: ")
            if len(height) > 0 and 0 < float(height) < 10:
                height_exact = float(height)
                break
            else:
                print("Enter valid height")
                program_exit()
                continue
        fo()

        print("Weight:", weight + "kg")
        print("Height: ", height + "m")
        program_exit()
    else:
        print("Enter valid Name")
        program_exit()
        continue

# Done          Ink
