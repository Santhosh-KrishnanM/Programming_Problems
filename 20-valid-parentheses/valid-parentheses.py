class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                p.append(c)
            elif c == ')' or c == ']' or c == '}':
                if not p:
                    return False
                top = p[-1]
                if c == '}' and top != '{' or c == ')' and top != '(' or c == ']' and top != '[':
                    return False
                p.pop()
        return not p
