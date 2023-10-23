from string import *
from itertools import product

value = ascii_letters + digits + punctuation

with open("password2.txt", "a") as p:
    for i in range(6, 10):
        for j in product(value, repeat=i):
            word = "".join(j)
            p.write(word)
            p.write("\n")
