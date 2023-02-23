print("Hello, Ink")

def check():
    namesake = input("Enter Name: ")
    
    if namesake.isalpha() or namesake.isprintable() and namesake.islower():
        namesake = namesake.strip()
        print("Happy Birthday, ", namesake)
    else:
        errormsg = namesake.islower()
        print("Enter ", namesake.upper(), " in lowercase bitch!!!", errormsg)
        check()

    return namesake # though don't know

check()

exit()

# G This
