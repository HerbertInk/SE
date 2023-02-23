print("*******Inputs*******")

print(" 20 \n Bitcoin \n Twitter")

# apple = int(input("9 < x < 24: "))
him = 20
x = him - 10
print(x)

print("*******str slicing*******")
string = "    HerbertNInk200    ".lower()                 # negative effect on string reading; it's direct from the end
print(string)
a = x - 3
print("b: ", a)
slice = string[a]
print("str slice: ", slice)
print("str length: ", len(string))

print("*******Looping thru str*******")
index = 0
while index < len(string):
    letter = string[index]
    print(index, letter)
    index = index + 1

print("*******Trial*******")
y = 4
trial = string[y]
print(trial)

print("*****for loop*****")
for letter in string:
    print(letter)

print("*******Looping & counting*******")
count = 0
for letter in string:
    if letter == 'n':
        count = count + 1
print(count)

print("****Looking deeper into 'in' ****")
for letter in 'Ink':
    print(letter)

print("****More on String slicing****")
print(string[:])                        # string
print(string[12:15])                    # Ink
print(string[0:12])                     # herbertn
print(string[12:27])                    # Ink20
print(string[7:8])                      # b

print("****String conc +****")
crypto = "Bitcoin"
social = "Twitter"
s = crypto + ' ' + social
print(s)

print("****in Logical operator +****")
crypto_c = "Bitcoin"
social_s = "t"
if social_s in social:
    print(social, " @BTCKnight_Ink")
for letter in crypto:
    if letter == 'B':
        print(crypto, " Is For Humanity")

print("****String comparison****")

lites = "Litecoin"
if lites == 'Litecoin':
    print("It's 84")
    # Another 1
if crypto > "Bitcoin":
    print('#' + crypto + ', comes before Bitcoin.')
elif crypto < 'Bitcoin':
    print("Anonymous")
else:
    print("Thankful to Satoshi")

print("****String Library****")
lib = "Invention And Innovation"
q = lib.lower()
w = type(lib)
e = dir(lib)
r = lib.find('ti')
t = lib.find('xx')      # -1
u = lib.find('n')

print(f"{q} \n {w} \n {e} \n"
      f"{r} \n {t}\n {u}")      # u 6


print("****Search & Replace****")
lens = "    Is crypto sound money? \nYes, it's    "
b = lens.replace("crypto", "Bitcoin")
print(b)

print("****Stripping str****")
i = lens.lstrip()
n = lens.rstrip()
k = lens.strip()
print(f"{i} \n {n} \n {k}")

print("****Prefixes****")
start = "Forex Markets".lower()
r = start.startswith("Forex")
d = start.endswith("kets")
print(f"{r} \n{d}")

print("****Parsing & Extracting****")
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
f = data.find("@")
g = data.find(' ', f)
print(f"@ Position; {f} \nFirst space after @; {g}")
host = data[f+1:g]
print("Host: ", host)

# index = 0
# while index < len(string):
#    letter = string[index]
#    print(index, letter)
#    index = index + 1
