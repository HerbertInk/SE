# Python objects.>> [strings]__
# functions that are built into the object__are available to any instance of the object.
# both data (the actual string itself) and methods.
# dir__lists the methods available for an object.
# type__shows the type of an object
# dir__shows the available methods.
word_st = input("Enter text: ")    # .lower()
r = type(word_st)
v = dir(word_st)
print(r)
print(v)
word_sst = word_st.lower()
print(word_sst)
cap = word_st.capitalize()
print(cap)
# help(str.capitalize)
# Help on method_descriptor:        capitalize(...)           S.capitalize() -> str
# Return a capitalized version of S, i.e. make the first
# character have upper case and the rest lower case.
# __help to get some simple documentation on a method

