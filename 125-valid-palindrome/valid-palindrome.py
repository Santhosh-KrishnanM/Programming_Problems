class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1 = "".join(char for char in s if char.isalnum()).lower()
        print(s1[::],"\n",s1[::-1])
        if(s1[::] == s1[::-1]):
            return True
        return False
        print(s1[::-1])