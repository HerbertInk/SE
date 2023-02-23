# Calling a method is similar to calling a function     (it takes arguments and returns a value)
# but the syntax is different.      We call a method by appending the method name to the variable name
# using the period as a delimiter       Like>> Instead of the function syntax upper(word),
# it uses the method syntax word.upper().
print("Ink is dope, the fam is great, this greatness upon the creator")
print("Invocation")
word_st = input("Enter text: ")
word_st = word_st.capitalize()   # .lower()
new_word = word_st.upper()
print(new_word)
# form of dot notation specifies the name of the method, upper ,
# and the name of the string
# to apply the method to, word .
# () indicate that this method takes no argument.
# A method call is called an invocation__invoking upper on the word .
print("Find")
print("Default:\n   Great")
letter_find = input("Enter the text to find: ")
letter_find = letter_find.lower()       # .capitalize has got an impact for the word_st update
index = word_st.find(letter_find)
print(index)
# __searches for the position of one string within another:
# __invoke find on word__pass the letter___looking for as a parameter.
# __find method can find substrings as well as characters:
print("Sub strings & characters")
index_v = word_st.find(letter_find)
print(index_v)
# It can take as a second argument the index where it should start:
print("2nd Arg. start".upper())
index_x = word_st.find(letter_find, 10)
print(index_x)
print("Strip Method".upper())
# to remove white space (spaces, tabs, or newlines) from the beginning and end of a string
strip_m = word_st.strip()
print(strip_m.capitalize())
print("Startswith Method".upper())
# return boolean values.
print("Default:\n   iNk")
start_w_find = input("Enter the word to find: ")
start_w_find = start_w_find.capitalize()
start_word = word_st.startswith(start_w_find)
print(start_word)
print("Default:\n   I")
start_let_find = input("Enter the letter to find: ")
start_let_find = start_let_find.capitalize()
start_letter = word_st.startswith(start_let_find)
print(start_letter)
# line.lower().startswith('h')
print("Write an invocation that counts\nthe number of times the letter a occurs in a string.")
print("Exe4 Strings Chapter 6")
