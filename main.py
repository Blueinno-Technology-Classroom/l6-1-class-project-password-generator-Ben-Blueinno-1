import random
import string

pw = ''

pw_len = int(input('password length: '))

for i in range(pw_len):
    pw += random.choice(string.printable)

print(pw)
