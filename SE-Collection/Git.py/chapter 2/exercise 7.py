# ask user for the amount to change
amount = float(input("enter amount to make change :"))

print("change is....")

# full twenties gained out of the entered amount
twenties = amount // 20
remainder_20 = amount % 20


# full 10 gained out of the remainder of 20
tens = remainder_20 // 10
remainder_ten = remainder_20 % 10

# full 5 gained out of the remainder of 10
fives = remainder_ten // 5
remainder_five = remainder_ten % 5

# full 1 s out of the remainder 5
ones = remainder_five // 1
remainder_ones = remainder_five % 1


# get full quarter out of remainder of ones
quarter = remainder_ones // 0.25
remainder_quarter = remainder_ones % 0.25

# get dimes out of the remainder of quarters
dimes_n = remainder_quarter // 0.1
remainder_dime = remainder_quarter % 0.1

# get nickles out the remainder of dimes
nickels = remainder_dime // 0.05
remainder_nickle = remainder_dime % 0.05


# get penny out the remainder of nickles
penny_n = remainder_nickle // 0.01

print(round(twenties), "Twenties")
print(round(tens), "Tens")
print(round(fives), "Fives")
print(round(ones), "Ones")
print(round(quarter), "Quarters")
print(round(dimes_n), "Dimes")
print(round(nickels), "Nickles")
print(round(penny_n), "Pennies")


