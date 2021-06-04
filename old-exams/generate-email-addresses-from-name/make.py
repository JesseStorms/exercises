
with open("input.txt") as f:
    with open("output.txt", "w+") as out:
        for line in f:
            split = line.split()
            fname = split[0].lower()
            lname = "".join(split[1:]).lower()
            out.write(f"{fname}.{lname}@student.ucll.be\n")
        out.close()
    f.close()
