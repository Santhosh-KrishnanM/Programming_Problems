class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 
        
        last_seen = {}
        
        for i in range(1, n + 1):
            char = s[i - 1]
            dp[i] = (dp[i - 1] * 2) % MOD
            
            if char in last_seen:
                prev_idx = last_seen[char]
                dp[i] = (dp[i] - dp[prev_idx - 1] + MOD) % MOD
                
            last_seen[char] = i
            
        return (dp[n] - 1 + MOD) % MOD