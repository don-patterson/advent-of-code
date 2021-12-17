from math import prod
from itertools import islice

_glob = {"sum": 0}


def input():
    with open("input-16.txt") as f:
        while (c := f.read(1)) not in ("", "\n"):
            yield from f"{int(c, 16):04b}"


def read(bitstream, n):
    return "".join(islice(bitstream, n))


class Packet:
    def __init__(self, version, type):
        _glob["sum"] += int(version, 2)
        self.version = version
        self.type = type
        self.children = []
        self.literal = None

    def add(self, packet):
        self.children.append(packet)

    @property
    def op(self):
        if self.type == "000":
            return sum
        if self.type == "001":
            return prod
        if self.type == "010":
            return min
        if self.type == "100":
            return lambda v: self.literal
        if self.type == "011":
            return max
        if self.type == "101":
            return lambda v: 1 if v[0] > v[1] else 0
        if self.type == "110":
            return lambda v: 1 if v[0] < v[1] else 0
        if self.type == "111":
            return lambda v: 1 if v[0] == v[1] else 0
        raise ValueError("unsupported type!")

    @property
    def value(self):
        return self.op([c.value for c in self.children])


def read_packet(bits):
    packet = Packet(version=read(bits, 3), type=read(bits, 3))
    if packet.type == "100":
        packet.literal = read_literal(bits)
    else:
        read_operator(bits, root=packet)
    return packet


def read_literal(bits):
    message = []
    while read(bits, 1) == "1":
        message.append(read(bits, 4))
    message.append(read(bits, 4))
    return int("".join(message), 2)


def read_operator(bits, root):
    if read(bits, 1) == "0":
        bit_length = read(bits, 15)
        packet_bits = read(bits, int(bit_length, 2))
        while packet_bits:
            # annoying, but not sure how else to do this right now
            stream = iter(packet_bits)
            root.add(read_packet(stream))
            packet_bits = "".join(stream)
    else:
        packet_count = int(read(bits, 11), 2)
        for _ in range(packet_count):
            root.add(read_packet(bits))


root = read_packet(input())

print("1:", _glob["sum"])
print("2:", root.value)
