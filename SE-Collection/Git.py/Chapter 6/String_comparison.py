word_st = input("Enter text: ")    # .lower()
word_nd = input("Enter the text for comparison: ")
if word_st < word_nd:
    print('Your word,'.upper() + word_st + ', comes before'.upper(), word_nd, '.')
elif word_st > word_nd:
    print('Your word,'.upper() + word_st + ', comes after'.upper(), word_nd, '.')
elif word_st == word_nd:
    print('Good'.upper())
else:
    print('All right,'.upper())
# To address this problem_convert strings to a
# standard format__all lowercase, before performing the comparison
