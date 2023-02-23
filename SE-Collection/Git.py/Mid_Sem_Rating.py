# rate
try:
    print('Enter your mid semester...rating\nRating ranges from 0 to 5')
    x = float(input('Your rating:\n'))
    print(x, 'Star')
    if not(0 < x <= 5):
        print("Sorry\n")
        print('Ink')
        exit()
    else:
        if 0 < x <= 5:
            print('Keep the move to 4.8\n')
        if x > 2.5:
            print('Hold on, keep coding')
            print('Have your analysis\nOf concepts summarized\n\nBlessings\nInk*')
        elif x > 2:
            print('Make research\n\nInk')
        elif x > 1.5:
            print('You be reading\n\nInk')
        elif x > 1:
            print('No one will blame you for consulting')
        elif x >= 0.5:
            print('Save your ass\n\nInk')
        elif x < 0.5:
            print('Devise means out of the rabbit hole')
        else:
            print("Blessings in Mid semester\n\n"'Ink')
            print('Move on')
            exit()
except:
    print("Error, Please insert a numeric input")
    exit()
