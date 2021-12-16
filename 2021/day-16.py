from math import prod

with open("input-16.txt") as f:
    input = f.read().strip()


class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type

        # probably could make Literal and Operator subclasses...oh well
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

    def traverse(self):
        yield self
        for child in self.children:
            yield from child.traverse()

    def __repr__(self):
        return f"Packet(type={self.type}, value={self.value})"


def split(string, length):  # abcdef, 2 -> ab, cdef
    return string[:length], string[length:]


def to_bits(hex_string):
    return "".join(f"{int(h, 16):04b}" for h in hex_string)


def read_packet(bits):
    version, bits = split(bits, 3)
    type, bits = split(bits, 3)

    packet = Packet(version, type)

    if type == "100":
        packet.literal, bits = read_literal(bits)
    else:
        bits = read_operator(bits, root=packet)
    return packet, bits


def read_literal(bits):
    message = []
    while True:
        chunk, bits = split(bits, 5)
        assert len(chunk) == 5, "missing/corrupted literal value?"
        more, value = split(chunk, 1)
        message.append(value)
        if more == "0":
            break
    return int("".join(message), 2), bits


def read_operator(bits, root):
    mode, bits = split(bits, 1)
    if mode == "0":
        bit_length, bits = split(bits, 15)
        packet_bits, bits = split(bits, int(bit_length, 2))
        while packet_bits:  # read from packet_bits only, don't consume from bits
            packet, packet_bits = read_packet(packet_bits)
            root.add(packet)
    else:
        packet_length, bits = split(bits, 11)
        for _ in range(int(packet_length, 2)):  # consume from bits
            packet, bits = read_packet(bits)
            root.add(packet)
    return bits


def version_sum(root):
    return sum(int(packet.version, 2) for packet in root.traverse())


examples = {
    "literal 2021": "D2FE28",
    "operator(10,20)": "38006F45291200",
    "operator(1,2,3)": "EE00D40C823060",
    "version sum 16": "8A004A801A8002F478",
    "version sum 12": "620080001611562C8802118E34",
    "version sum 23": "C0015000016115A2E0802F182340",
    "version sum 31": "A0016C880162017C3686B18A3D4780",
    "value 3": "C200B40A82",
    "value 54": "04005AC33890",
    "value 7": "880086C3E88112",
    "value 9": "CE00C43D881120",
    "value 1": "D8005AC2A8F0",
    "value 0": "F600BC2D8F",
    "also 0": "9C005AC2F8F0",
    "also 1": "9C0141080250320F1802104A08",
}

# for title, hex_string in examples.items():
#     bits = to_bits(hex_string)
#     print("starting example", title, hex_string, bits)
#     packet, leftover = read_packet(bits)
#     print("sum:", version_sum(packet), "value:", packet.value, "leftover:", leftover)


root, leftover = read_packet(to_bits(input))

print("1:", version_sum(root))
print("2:", root.value)
