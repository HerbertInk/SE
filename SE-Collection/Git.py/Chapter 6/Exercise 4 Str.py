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
# This is a Try and Error kind of code for Exercise 4 code Chapter 6
# Not pushed on the earlier push to Github
