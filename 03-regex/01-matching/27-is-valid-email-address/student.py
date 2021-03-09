# Write your code here
import re

def is_valid_email_address(s):
    return re.fullmatch(r'^([0-9A-z.]+@)((student\.)?ucll\.be)',s)