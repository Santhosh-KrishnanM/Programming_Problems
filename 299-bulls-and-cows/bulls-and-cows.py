class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b, c = 0, 0
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                b += 1
        for i in set(secret):
            c += min(secret.count(i), guess.count(i))
        return f"{b}A{c-b}B"