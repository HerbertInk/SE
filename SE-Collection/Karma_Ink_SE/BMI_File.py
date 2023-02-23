print("*********Writing in a file**************")  # .....File lines^^^

while True:
    file_name = (input("Enter file name: ")).strip()

    if file_name == "":
        print("File name required")
        continue

    elif file_name.startswith("Ink"):
        line4 = "Trial"

        write_file = open(file_name, 'w')  # Ink21
        print(write_file)

        print("File length:", write_file.write(line4))

        print("On exit~:", write_file.close())
        print("Lil:\n", file_name, "\n", (open(file_name)).read())

        # for text in open(file_name): Prints text in file as in code
        #    print("In loop: ", text)
        break    # For 'for' loop; indent of break prints 1 line of a file
        # For 'elif' continue not here
    elif print("Must begin with 'Ink', yours is", file_name + "!!!"):
        continue

    print("**********Reading the file************")

    while True:
        file_name_r = (input("Enter file name to read: ")).strip()

        if file_name_r == "":
            print("File name required")
            continue

        elif file_name_r.startswith("Ink"):
            read_file = open(file_name_r, 'r')  # , 'w'  # Ink21
            print(read_file)
            # print("Lil:\n", file_name, "\n", (open(file_name)).read())
            print("On exit~:", read_file.close())

        elif print("Must begin with 'Ink', yours is", file_name_r + "!!!"):
            break


# for text in open(file_name): This for loop prints file as much as the lines inside a file
# For small sized files

# for text in open(file_name): This for loop prints file as much as the lines inside a file
# For small sized files


# With files;

# Handle: open read write close
