
with open("input.txt") as f:
    with open("output.txt", "w+") as out:
        for line in f:
            if line[0].lower() == "u":
                out.write(f"{line.lower().strip()}@ucll.be\n")
            else:
                out.write(f"{line.lower().strip()}@student.ucll.be\n")
        out.close()
    f.close()
