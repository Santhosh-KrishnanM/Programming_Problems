class Solution:
    def convert(self, num):
        total = 0
        zero_ascii = ord('0')  # 48
    
        for char in num:
            if '0' <= char <= '9':
                digit_value = ord(char) - zero_ascii
                total = (total * 10) + digit_value
            else:
                raise ValueError(f"Invalid character: {char}")
            
        return total

    def int_to_string(self, num):
        if num == 0:
            return "0"
        
        is_negative = False
        if num < 0:
            is_negative = True
            num = -num
        
        result_str = ""
        while num > 0:
            remainder = num % 10
            char = chr(ord('0') + remainder)
            result_str = char + result_str
            num //= 10
        
        return "-" + result_str if is_negative else result_str

    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = self.convert(num1), self.convert(num2)
        s = n1 * n2
        return self.int_to_string(s)