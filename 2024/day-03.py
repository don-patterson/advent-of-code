import re
from os.path import dirname
with open(dirname(__file__) + "/input/03.txt") as f:
    input = f.read()

print("1:", sum(int(a)*int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)))

input = re.sub(r"don't\(\).*?($|do\(\))", "", input.replace("\n", ""))
print("2:", sum(int(a)*int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)))
