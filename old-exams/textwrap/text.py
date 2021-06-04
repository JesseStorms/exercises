import textwrap
wap = textwrap.TextWrapper(width=40)
with open("input.txt") as f:
    with open("output.txt", "w+") as out:
        for line in f:
            out.write(wap.fill(text=line))
        out.close()
    f.close()
