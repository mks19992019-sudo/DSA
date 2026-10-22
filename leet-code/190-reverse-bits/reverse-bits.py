class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)
        binary = binary[2:].zfill(32)
        rev_binary = binary[::-1]
        return int(rev_binary,2)
        