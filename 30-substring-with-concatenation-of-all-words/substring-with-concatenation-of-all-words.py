class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:  # Edge case: words list empty
            return []
        tot_len = len(words) * len(words[0])
        result = []
        word_count = Counter(words)          
        for i in range(len(s) - tot_len + 1):
            # Extract substring and split into chunks
            substr = s[i:i+tot_len]
            chunks = [substr[j:j+len(words[0])] for j in range(0, tot_len, len(words[0]))]
            
            # Check if chunk frequencies match target
            if Counter(chunks) == word_count:
                result.append(i)
                
        return result