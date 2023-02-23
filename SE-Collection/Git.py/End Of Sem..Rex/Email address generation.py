# Extended version of Username generation
# Full_name inputs
surname = input("Enter Surname: ")
given_name = input("Enter Given Name: ")
# email_address = input("Email address: ")
# generation of email address
welcome = "Here's the preferred choice of E-mail address Ink"
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import random
t = random.choice(int_list)
the_slice = surname[:2]
choice_of_email = (given_name.lower() + the_slice.lower() + str(t) + "@gmail.com")
print("Hello,", given_name)
print(welcome)
print("Preferred E-mail Address:\n", choice_of_email)
