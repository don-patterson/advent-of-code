with open("input/01.txt") as f:
    input = f.read()

print("1:", input.count("(") - input.count(")"))
print("2:", 1797)  # used vim "%" to match parens until I hit an "opening )" haha
