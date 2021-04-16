import sys
import re

def editFile(filename):
    with open(filename, 'r') as file:
        content = file.read()

    content = re.sub(r'#.*$', '', content, flags=re.MULTILINE)
    
    with open(filename,'w') as output:
        output.write(content)

for file in sys.argv[1:]:
    editFile(file)