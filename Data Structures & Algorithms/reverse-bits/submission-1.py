class Solution:
    def reverseBits(self, n: int) -> int:
        s = 0
        for i in range(32):
            ## isolate the bit you want
            bit = (n >> i) & 1
            ## shift it by the power you want and add to res
            s += (bit << (31 - i))     

        return s   