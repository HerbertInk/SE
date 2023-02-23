# User inputs
# Staff_ID Name
# FT M_Basic & statutory
# PT Hrs_Worked
# Exit

import time

# =================================================================================
#                  TIME
# ================================================================================
localtime = time.asctime(time.localtime(time.time()))


def main():
    global worked_hr_part, full_month_fee, full_month_salary, staff_name, staff_no, net_pay, tax,\
        hourly_pay, fixed_percent, total_pay, full_tax, full_net_pay

    #   store = ['FT' or 'PT']

    while True:
        print("\n************Worker's ID************")
        user_entry = input("Enter Staff ID: ")      # Check for input
        if 0 < len(user_entry) < 7:

            if user_entry.isalnum() and user_entry.startswith('FT'.upper()) or user_entry.startswith('FT'.lower())\
                    or user_entry.startswith('fT') or user_entry.startswith('FT'.capitalize()):

                user_entry = user_entry.lower()

                if user_entry.isalnum():
                    staff_no = user_entry.upper()
                    break

            elif user_entry.startswith('PT'.upper()) or user_entry.startswith('PT'.lower()) \
                    or user_entry.startswith('pT') or user_entry.startswith('PT'.capitalize()):
                staff_no = user_entry.upper()
                break

            else:
                print("Invalid Staff ID\nCapitalize the staff ID\n"
                      "Begin with\n FT >>> Full time Or\n PT >>> Part time")
        else:
            print("Invalid ID\nOut of limits[Maximum of 5 characters required]")
            continue
    # when the above while loop finds a break it quits the loop and; it has stored a code

        # User Name
    while True:
        print("************Your Name************")
        F_name = input("Enter First name: ").strip()
        L_name = input("Enter Last name: ").strip()
        FL_list = F_name and L_name

        if 0 < len(FL_list) < 45 and F_name.isalpha() and L_name.isalpha():
            staff_name = str(F_name) + " " + str(L_name)
            break

        else:
            print("Invalid input, Enter correct name")
            continue

        # Full Time: Monthly salary
    if user_entry.startswith('FT'.upper()) or user_entry.startswith('FT'.lower()) \
            or user_entry.startswith('fT') or user_entry.startswith('FT'.capitalize()):

        while True:
            print("************Full Time************")
            monthly_basic = input("Enter Monthly salary: $")

        # Check for salary input and validity
            if len(monthly_basic) > 0 and float(monthly_basic) >= 100:
                full_month_salary = float(monthly_basic)
                break

            else:
                print("Invalid salary input, Must be $100 and above")
                continue

        # Statutory deductions
        while True:
            print("************Full Time fees************")
            statutory = input("Enter percentage fee charged: ")

            if len(statutory) > 0 and 0 < float(statutory) >= 25:
                full_month_fee = float(statutory)

                full_tax = (full_month_fee * full_month_salary) / 100
                full_net_pay = full_month_salary - full_tax
                break

            else:
                print("Invalid full time fee charged\nPercentage fee must be 25% and above!!!")
                continue

        # Part Time: Hours worked
    elif user_entry.startswith('PT'.upper()) or user_entry.startswith('PT'.lower()) \
            or user_entry.startswith('pT') or user_entry.startswith('PT'.capitalize()):

        while True:
            print("************Part Time work hours************")
            hours_worked = input("Enter hours worked: ")

            if len(hours_worked) > 0 and hours_worked.isdigit() and 0 < int(hours_worked) < 744:
                worked_hr_part = int(hours_worked)

                hourly_pay = 2500
                total_pay = hourly_pay * worked_hr_part
                fixed_percent = 30
                fixed_percent = float(fixed_percent)

                tax = (fixed_percent * total_pay) / 100
                net_pay = total_pay - tax
                break

            else:
                print("Invalid hours worked. The maximum hours in a month is 744 hrs")
                continue

        # Print statements
    print("\n           Payment statement          ")
    print("************Worker's details************\n")
    print("Staff Code: ", staff_no, "\nStaff Name: ", staff_name)
        # Full Time
    if user_entry.startswith('FT'.upper()) or user_entry.startswith('FT'.lower()) \
            or user_entry.startswith('fT') or user_entry.startswith('FT'.capitalize()):
        print("\n************Full time payment************\n")

        print("Full Time Monthly Salary Basic: $", full_month_salary)
        print("Percentage tax of monthly salary: ", full_month_fee, "%", "\nTax amount: $", full_tax, "\n")
        print("Net salary: ", full_net_pay)

        print("\nTime Stamp:", localtime)

        # Part Time
    elif user_entry.startswith('PT'.upper()) or user_entry.startswith('PT'.lower()) \
            or user_entry.startswith('pT') or user_entry.startswith('PT'.capitalize()):

        print("\n************Part time payment************\n")
        print("Part time hours worked: ", worked_hr_part, "Hours")
        print("Payment per hour $", hourly_pay, "\nTotal pay: $", total_pay)
        print("Percentage tax of Total pay", fixed_percent, "%", "\nTax amount: $", tax, "\n")
        print("Net pay: $", net_pay)

        print("\nTime Stamp:", localtime)

        # The Exit
    while True:
        print("\n**********Would you like to exit the program**********\n")
        the_exit = input("Enter Done >>> For Exiting the program\n"
                         "      Next >>> For another staff member: ").lower().strip()
        if the_exit == "Done".lower():
            exit()
        elif the_exit == "Next".lower():
            main()


# Call main
main()
        # By
print("\n********************Ink********************\n")

# Finalizing of staff_ID with 'isalnum' effect and the 'exit' >>> For tomorrow Sep 24,
# Thankful Ink
