#This program can generate a 8 character password using uppercase_lowercase_special char with no duplicate characters in the password

import random

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?abcdefghijklmnopqrstuvwxyz"
passwordlen = 8
p =  "".join(random.sample(s,passwordlen ))
print("The suggested password is = ",p)