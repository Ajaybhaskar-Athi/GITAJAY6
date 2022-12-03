###print random password when user enters ;length of password



import random
import string
def password(l):
    if l>=12:
        a=string.ascii_letters+ string.digits+ string.punctuation
        result=''.join(random.choice(a) for i in range(l))
        print("random password = ",result)
    else:
        print("Invalid")
l=int(input("Enter the length for the password: "))
password(l)
