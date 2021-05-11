
attenders = []
absent = []
with open("attending.txt") as f:
    for line in f:
        line = line.strip().lower()
        attenders.append(line)
with open("all.txt") as f:
    for line in f:
        line = line.strip().lower()
        if line not in attenders:
            absent.append(line)
    f.close()
with open("absentees.txt", "w+") as f:
    f.write("\n".join(absent))
    f.close()

