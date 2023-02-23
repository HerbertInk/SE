# Billing
def salary_calculator(Staff_ID, salary):
    while True:

        if Staff_ID.startswith('FT'.upper()) or Staff_ID.startswith('FT'.lower()):
            percent = int(input("Enter percentage fee charged: "))
            if percent > 0:

                tax = (percent * salary) / 100
                net_salary = salary - tax
                print("Percentage fee: ", percent, "%")

                return float(net_salary)
            else:
                print("Invalid percentage fee")
        else:
            print("Invalid ID!!!")
            continue


salary_calculator()
