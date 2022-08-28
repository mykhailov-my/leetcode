from collections import Counter


class Solution:
    """
    Status -> Solved by myself

    Tags -> Sliding window, Counter

    Time complexity -> O(S1*S2)
    Space complexity -> O(S2)

    Solution
    1. if s1 bigger s2 -> return false, it;s impossible to be true
    2. Count characters in s1
    3. init left, right pointer and window counter
    4. count charater in window counter that in s1 counter
    5. iterate bwith sliding window by s2
        6. decrement window counter of left - 1
        7. increment window counter of right
        8. if all keys and values from s1 counter equal window counter's -> return true
        9. increment left and right
    10. return false

    Notes 
    not best solution
    34% for time
    95% for memory
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        left = 0
        right = len(s1) - 1
        window_counter = {}
        for char in s2[left: right + 1]:
            if char in s1_counter:
                window_counter[char] = window_counter.get(char, 0) + 1

        while right < len(s2):
            if left and s2[left - 1] in s1_counter:
                window_counter[s2[left -1]] -= 1
            if left and s2[right] in s1_counter:
                window_counter[s2[right]] = window_counter.get(s2[right], 0) + 1
            if all(window_counter.get(key) == s1_counter[key] for key in s1_counter):
                return True
            left += 1
            right += 1
        return False


if __name__ == '__main__':
    s1 = 'ab'
    s2 = 'eidbaooo'
    # s2 = 'dfsdcsdba'
    # s1 = 'adc'
    # s2 = 'dcda'
    # s1 = 'plasma' # False
    # s2 = 'altruism'
    sol = Solution()
    res = sol.checkInclusion(s1, s2)
    print(f'Result --> {res}')
