class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0

        for num in range(1,n+1):
            x = num
            valid = True
            changed = False

            while x > 0:
                digit = x % 10

                if digit == 3 or digit == 4 or digit == 7:
                    valid = False
                    break

                if digit == 2 or digit == 5 or digit == 6 or digit == 9:
                    changed = True

                x //= 10

            if valid and changed:
                count += 1

        return count