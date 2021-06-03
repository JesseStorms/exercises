import re

with open("input.txt") as file:
    with open("output.txt", "w+") as target:
        for line in file:
            if re.match(r"(\+32-|0)(4[5-9]\d)-(\d{2})-(\d{2})-(\d{2})$",line):
                target.write(line)
    target.close()
file.close()

