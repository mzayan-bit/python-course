import random 
import string 

choices = string.ascii_letters + string.digits + string.punctuation
pass_len = 12 
password = ""

for i in range(pass_len):
    password += random.choice(choices)

print("Your Random Password is : ",password)