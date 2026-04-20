class Solution:
        def maximumBinaryString(self, binary: str) -> str:
            leading_ones = binary.find('0')
            if leading_ones < 0:
                return binary
            n = len(binary)
            zeros = binary.count('0')
            rest_ones = n - leading_ones - zeros
            return '1'* (leading_ones + zeros - 1) + '0' + '1' * rest_ones