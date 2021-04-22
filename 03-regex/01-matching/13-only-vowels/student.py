# Write your code here
import re

def only_vowels(s):
    return re.fullmatch("([aeiou])*",s)