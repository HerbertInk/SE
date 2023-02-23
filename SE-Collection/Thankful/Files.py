handle = open("mbox-short.txt")          # 'r' 'w'
print('File handle: ', handle)

print("****Line count ****")
count = 0
for line in handle:
    count = count + 1
print('Line Count:', count)

print('****File Handle as a Sequence****')
handle = open("mbox-short.txt")          # 'r' 'w'
text = "Date"
for text in handle:
    print("Ink")
print(len(text))

print("****The read method on the file handle****")         # File is relatively small
handle = open("mbox-short.txt")          # 'r' 'w'
# inp = handle.read()
# print(len(inp))
# print(inp[:30])
print("!st search thru~: ", len(handle.read()))             # will It "file data" fit comfortably in the main memory
# print(len("2nd: ", handle.read()))                        # abstractmethod

print('****File Handle as a Sequence; TEXT COUNT IN HANDLE****')
handle = open("mbox-short.txt")          # 'r' 'w'
text = "date"
count = 0
for text in handle:
    count = count + 1
print('Line Count:', count)             # tab effect

print('****Searching through a file: Prefix “From:”****')

handle = open("mbox-short.txt")          # 'r' 'w'
print("!st search thru~: ", len(handle.read()))             # will It "file data" fit comfortably in the main memory
# print(len("2nd: ", handle.read()))                        # abstractmethod

handle = open("mbox-short.txt")          # 'r' 'w'
count = 0
for line in handle:
    line = line.rstrip()        # double spacing fix

    # if line.startswith("From:"):
    #    count = count + 1
    #   print("Initial:  ", line)              # Invisible new line character
# print(count)

    # Skip uninteresting lines
    if not line.startswith("From:"):
        continue
    # process our interesting line
    print("Process our interesting line:  ", line)

    # Find string method
    if line.find("uct.ac.za") == -1: continue
    print("Find str method:  ", line)

print("*********Final search and count**************")
handle = open("mbox-short.txt")          # 'r' 'w'
count = 0
for line in handle:
    line = line.rstrip()        # double spacing fix
    if not line.startswith("From:") or line.find("uct.ac.za") == -1:
        continue
    print("Simulate text editor search", line)
    count = count + 1
print("Search count", count)

print("*********Prompt for file input**************")
file_input = input("Enter file name mbox-short.txt: ")     # mbox-short.txt
try:
    file_handle = open(file_input)
except:
    print('File cannot be opened:', file_input)
    exit()
count = 0
for line in file_handle:
    line = line.rstrip()
    if line.startswith("From:"):
        count = count + 1
    print(line)
print(count)
print("There were", count, "subject lines in", file_input)
# except:
#    print('File cannot be opened:', file_input)
#    exit()
