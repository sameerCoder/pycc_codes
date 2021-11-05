# opening d drive file from c file.

with open(r"D:/ddrivetext.txt") as fileo:
    lines=fileo.readlines()
    for l in lines:
        print(l)
