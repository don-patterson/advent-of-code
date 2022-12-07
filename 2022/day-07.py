sizes = []


class Dir:
    def __init__(self, name):
        self.name = name
        self.contents = {}
        self._size = None

    @property
    def size(self):
        if self._size is None:
            self._size = sum(
                v if type(v) is int else v.size for v in self.contents.values()
            )
            sizes.append(self._size)
        return self._size


root = Dir("/")
path = [root]

with open("input/07.txt") as f:
    for line in f:
        pwd = path[-1]
        match line.split():
            case ["$", "cd", "/"]:
                path[:] = [root]

            case ["$", "cd", ".."]:
                path.pop()

            case ["$", "cd", dir]:
                if dir not in pwd.contents:
                    print("should this happen?")
                    pwd.contents[dir] = Dir(dir)
                path.append(pwd.contents[dir])

            case ["$", "ls"]:
                pass

            case ["dir", dir]:
                if dir not in pwd.contents:
                    pwd.contents[dir] = Dir(dir)

            case [size, file]:
                pwd.contents[file] = int(size)

            case _:
                raise Exception("unmatched line")


total = root.size
print("1:", sum(size for size in sizes if size <= 100_000))


remaining_space = 70_000_000 - total
required_space = 30_000_000

print("2:", min(size for size in sizes if remaining_space + size >= required_space))
