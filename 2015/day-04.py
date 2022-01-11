from hashlib import md5

with open("input/04.txt") as f:
    input = f.read()


def hexhash(word):
    return md5(word.encode()).hexdigest()


for i in range(1, 99999999999):
    if hexhash(f"{input}{i}").startswith("00000"):
        print("1:", i)
        break

for i in range(1, 99999999999):
    if hexhash(f"{input}{i}").startswith("000000"):
        print("2:", i)
        break
