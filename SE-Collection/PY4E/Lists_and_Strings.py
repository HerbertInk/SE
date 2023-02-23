print("****Lists and Strings****")
time = "It's Year 2 Semester One"
char = list(time)
print("Char: ", char)
word = time.split()
print("Word: ", word)
print("Index_3: ", word[3:5])

print("***delimiter***")
time = "It's-Year-2-Semester-1"
delimiter = "-"
ltd_word = time.split(delimiter)
print("Delimiter split: ", ltd_word)

print("****join: invoke it > delimiter and pass list > parameter")
delimiter = " "
conc = delimiter.join(word)
print("Join: ", conc)

print("*****Parsing lines****")
file_hand = open('mbox-short.txt')
for line in file_hand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print("Date: ", words[2])

print("*****List arguments****")
