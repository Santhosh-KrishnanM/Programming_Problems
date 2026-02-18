import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True  # empty string matches empty pattern
        
        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                # Direct match or '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                
                # '*' case
                elif p[j - 1] == '*':
                    
                    # Zero occurrence
                    dp[i][j] = dp[i][j - 2]
                    
                    # One or more occurrence
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[m][n]