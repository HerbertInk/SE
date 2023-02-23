# A program takes a list modifies removing the first and last elements and returns non.(function chop)
# it also takes alist and returns  a new list  that contians all but the first and last elements(function middle)
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]


def chop(list_a):
    del list_a[0]
    del list_a[-1]


def middle(list_a):
    new_list = list_a[1:]
    del new_list[-1]
    return new_list


print(chop(list1))
print(middle(list2))
