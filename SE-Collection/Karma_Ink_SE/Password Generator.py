import string as s
from random import *
ch = s.ascii_letters + s.digits + s.hexdigits   # + s.punctuation
password = "".join([choices(ch)[0] for x in range(randint(8, 16))])
print(password)
