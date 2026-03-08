class Solution:
    def isNumber(self, s: str) -> bool:
        num, sym, exp, dec = False, False, False, False
        for i in s:
            if i >= '0' and i <= '9':
                num = True
            elif i == '+' or i == '-':
                if sym or num or dec:
                    return False
                else: 
                    sym = True
            elif i == 'e' or i == 'E':
                if exp or not num:
                    return False
                else:
                    exp = True
                    num, sym, dec = False, False, False
            elif i == '.':
                if dec or exp: return False
                else: 
                    dec = True
            else:
                return False
        return num