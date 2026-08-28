import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Validate if t can be formed by single-digit factors (2, 3, 5, 7)
        # Since the number must be zero-free, its digits can only be 1-9.
        temp = t
        for prime in [2, 3, 5, 7]:
            while temp % prime == 0:
                temp //= prime
        if temp > 1:
            return "-1"  # Contains a prime factor like 11, 13, etc.

        n = len(num)
        
        # Step 2: Precalculate required factors for remaining suffixes
        # suffix_req[i] will store the remaining part of t that needs to be satisfied
        # by the digits from index i to n-1.
        suffix_req = [1] * (n + 1)
        suffix_req[0] = t
        
        first_zero_idx = -1
        for i in range(n):
            if num[i] == '0':
                first_zero_idx = i
                break
            # Update the required t by dividing out the GCD with the current digit
            suffix_req[i + 1] = suffix_req[i] // math.gcd(suffix_req[i], int(num[i]))
            
        # If the original string is zero-free and already satisfies t
        if first_zero_idx == -1 and suffix_req[n] == 1:
            return num

        # Step 3: Backtrack from right to left to find where to increment
        limit = first_zero_idx if first_zero_idx != -1 else n - 1
        num_list = list(num)
        
        # Helper to check if a remaining target `rem` can fit into `available_slots`
        def can_fit(rem: int, available_slots: int) -> bool:
            # Greedily count how many 9s, 8s, ..., 2s are needed to divide out `rem`
            needed_slots = 0
            for d in range(9, 1, -1):
                while rem % d == 0:
                    rem //= d
                    needed_slots += 1
            return rem == 1 and needed_slots <= available_slots

        # Greedily search for the first position from the right where we can increment the digit
        for i in range(limit, -1, -1):
            curr_digit = int(num_list[i])
            
            # Try to increment the current digit to a higher value (from curr_digit + 1 to 9)
            for d in range(curr_digit + 1, 10):
                next_rem = suffix_req[i] // math.gcd(suffix_req[i], d)
                slots_left = n - 1 - i
                
                if can_fit(next_rem, slots_left):
                    # Found the turning point! Mutate the prefix digit.
                    num_list[i] = str(d)
                    
                    # Fill the remaining slots suffix greedily with smallest digits (1-9)
                    # to keep the overall number as small as possible.
                    for j in range(n - 1, i, -1):
                        for target_d in range(9, 1, -1):
                            if next_rem % target_d == 0:
                                next_rem //= target_d
                                num_list[j] = str(target_d)
                                break
                        else:
                            num_list[j] = '1'
                    return "".join(num_list)

        # Step 4: If no number of length n works, construct the smallest number of length n + 1
        # To do this, greedily pull out the largest possible digits from t from right to left
        ans = []
        for d in range(9, 1, -1):
            while t % d == 0:
                ans.append(str(d))
                t //= d
                
        # Fill up the rest with '1's to reach a length of n + 1 digits total
        total_len = max(n + 1, len(ans))
        ones_needed = total_len - len(ans)
        
        return "1" * ones_needed + "".join(reversed(ans))
