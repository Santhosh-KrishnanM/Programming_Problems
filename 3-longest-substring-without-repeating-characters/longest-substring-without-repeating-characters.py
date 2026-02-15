class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ds = set()
        left = 0
        long_substring = 0
        for right in range(len(s)):
            while s[right] in ds:
                ds.remove(s[left])
                left += 1
            ds.add(s[right])
            long_substring = max(long_substring, right - left + 1)
        return long_substring