# Lists are mutable
cloth = ['extra large', 'large', 'medium', '']
cloth[3] = 'small'
print('Hills: ', cloth)
i = 'small' in cloth
print("Response: ", i)

# Slices
print("Slicing: ", cloth[:2])

# List methods;
# append: adds new element to the list at the end_list
a = cloth.append('long')
print("Append: ", cloth)  # print(a) returns none
# extend: takes the list as an argument then adds all the elements.
color = ['blue', 'black', 'orange']
cloth.extend(color)
print("Extend: ", cloth)
# sort: arranges elements of the list from Low to High
cloth.sort()
print("Sort: ", cloth)

print('****Deletion****')
# pop: Know the index, modifies and returns the element that was removed.
index7 = cloth.pop(7)
print("Index7_Pop: ", cloth)
print("Index 7: ", index7)
# without index deletes and returns the last element
lst = cloth.pop()
print("Pop: ", cloth)
print("Last element: ", lst)
# del: don't need the removed value, > 1 use slice index
del cloth[2:]
print("del_: ", cloth)
# remove: Know element but not index
cloth.remove('black')
print("Remove: ", cloth)
