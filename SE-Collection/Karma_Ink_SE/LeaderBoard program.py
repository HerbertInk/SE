# digit = 0
while True:
    enter = int(input("Enter: "))

    if not 0 < enter < 10:
        print("Enter digit between 0 & 10")
        continue        # calls for re-entry when valid  ~'..not 0 < ent..'
    while True:
        if 0 < enter < 10:
            print(f"{enter}. ")
            enter = enter + 1
            continue    # break here 'exits code 0' without if execution
        break   # ~'calls for digit entry again even with end exit'  # exit() exits the program there & then
    break   # with end exit ~ keeps running, 'without 1st break'
exit()      # exit() without any break keeps the run

# with the two end breaks, Ink exit code 0
