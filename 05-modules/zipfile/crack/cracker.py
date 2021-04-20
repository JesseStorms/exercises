import os
import sys
import string
from zipfile import ZipFile

def all_letters():
    res = []
    for l1 in string.ascii_lowercase:
            for l2 in string.ascii_lowercase:
                    for l3 in string.ascii_lowercase:
                            for l4 in string.ascii_lowercase:
                                res.append(l1+l2+l3+l4)
    return res

def guess_password(zip, password):
    try:
        zip.read('file.txt', pwd=str.encode(password))
        return True
    except:
        return False

with ZipFile('crack.zip') as z:
    z.printdir()
    passwords = all_letters()
    for password in passwords:
        if(guess_password(z,password)):
            print("Password is: "+password)
            exit()
    print("can't find a password?")
    

