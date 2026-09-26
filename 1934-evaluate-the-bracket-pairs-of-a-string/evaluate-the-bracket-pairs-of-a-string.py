class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = {}

        for item in knowledge:
            mp[item[0]] = item[1]

        key = ""
        res = ""
        flag = False

        for ch in s:
            if ch == '(':
                flag = True
            elif ch == ')':
                if key in mp:
                    res += mp[key]
                else:
                    res += "?"

                flag = False
                key = ""
            elif flag:
                key += ch
            else:
                res += ch

        return res