X_1 = int(input("enter X_1:"))
Y_1 = int(input("enter Y_1:"))
X_2 = int(input("enter X_2:"))
Y_2 = int(input("enter Y_2:"))

diff_1_squared = (X_2 - X_1)**2
diff_2_squared = (Y_2 - Y_1)**2
sum_diffs = diff_1_squared + diff_2_squared
distance = sum_diffs**0.5

print("The distance is:", distance)
