"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""

# from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        # Counter()
        counter = {}  # store str->count
        # assighn first window
        for i in range(k):
            counter[s[i]] = counter.get(s[i], 0) + 1
        
        left = 0
        right = k
        # max_len = k
        while right < len(s):
            print(counter)
            # breakpoint()

            if s[right] in counter:
                counter[s[right]] += 1
                right += 1
            else:  # new unique symbol
                if len(counter) + 1 > k:  # we about to exceed k limit and have to move window right
                    left_char_count = counter[s[left]]  # decrease counter, if less 1, pop out
                    if left_char_count > 1:
                        counter[s[left]] -= 1
                    else:
                        counter.pop(s[left])
                    left += 1
                    counter[s[right]] = 1
                    right += 1
                else:  # just add it to counter
                    counter[s[right]] = 1
                    right += 1
        return right - left # return window size



if __name__ == '__main__':
    n = "eceba" # 3
    k = 2
    n = 'abacae' # 5
    k = 3
    n = 'xyxyaaabb' # 5
    k = 2
    sol = Solution()
    res = sol.lengthOfLongestSubstringKDistinct(n, k)
    print(f'Result --> {res}')  