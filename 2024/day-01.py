from os.path import dirname
left = []
right = []
with open(dirname(__file__) + "/input/01.txt") as f:
    for line in f:
        a,b = line.split()
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()

print("1:", sum(abs(a-b) for a,b in zip(left, right)))
print("2:", sum(a*right.count(a) for a in left))
