i = 1
n = input('Insert: ')
a = [n]
large = i


for i in a:
    if a > large:
        large = a
        print(large)
        break
    else:
        maximum = large
        print(maximum)
