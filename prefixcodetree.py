# Name   : Nguyễn Công Ngọc Tưởng
# Sid    : 17021120
# Course : MCN_INT3305_1

class PrefixCodeTree:
    def __init__(self):
        self.root = {}

    def insert(self, codeword, symbol):
        current_node = self.root
        for bit in codeword:
            if bit not in current_node:
                current_node[bit] = {}
            current_node = current_node[bit]
        current_node["symbol"] = symbol

    def decode(self, encodedData, datalen):
        encodedBin = ''.join(format(c, '08b') for c in encodedData)[0:datalen]
        result = ""
        current_node = self.root
        for e in encodedBin:
            current_node = current_node[int(e)]
            if "symbol" in current_node:
                result = result + current_node["symbol"]
                current_node = self.root
        return result


# Test program
codebook = {
    'x1': [0],
    'x2': [1, 0, 0],
    'x3': [1, 0, 1],
    'x4': [1, 1]
}

codeTree = PrefixCodeTree()

for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

message = codeTree.decode(b'\xd2\x9f\x20', 21)
# Expected result will be: x4x1x2x3x1x1x4x4x2x2
print(message)
