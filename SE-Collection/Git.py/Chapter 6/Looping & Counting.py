# Looping and counting
print("Looping and counting".upper())
word = "Herbert Ink Richard's".lower()
count = 0
for letter in word:
    if letter == 'r':
        # .lower() and .upper()
        count = count + 1
        # Difference of prints with indention
print(count)
# Exercise 3: Encapsulate this code in a function named count , and
# generalize it so that it accepts the string and the letter as arguments.
words_st = "Herbert Ink Richard's".lower()
word_count = words_st.count("r")
print(word_count)
print("BOOLEAN in operator")
# boolean operator that takes two strings and
# returns True if the first appears as a substring in the second:
in_op = "e" in words_st
print(in_op)
# Prompt form___exe.3 Push </>
print("Prompt form exe.3 Push </>")
words_nd = input("Enter text:\n").lower()
prompt = input("Enter letter to find its number of times:\n").lower()
word_count = words_nd.count(prompt)
print(word_count)
# Modification of mid sem exe.3 </>
print("Looping and counting\nExercise 3 pushed code")
txt_word = input("Enter a text:\n").lower()
character = input("Enter letter to find its number of times:\n").lower()
# def
# making a count of a letter in word


def count(text_word, character_s):
    count_wst = 0
    for text in text_word:
        if text == character_s:
            count_wst = count_wst + 1
            # break gives a zero print
            continue
    print(count_wst)


count(txt_word, character)
# The Input variables are the ones called
# The word count on additives ___The variable remains the same
# The for loop___in >>> parameter in the function definition
# The if statement___is equated == parameter in the function definition
# print ___Initial count_wst variable
