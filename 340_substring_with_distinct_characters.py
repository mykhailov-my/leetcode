

class Solution:
    """
    Status -> Solved by myself

    Time complexity -> O(N)
    Space complexity -> O(N)

    Solution
    1. Validation step, check if not 0 and k smaller then s
    2. first window has to k be length, so just count all chars from 0 to k
    3. iterate by string so right window border won't exceed string (right < len(s))
    4. check if counter exceed limit
        if yes -> move window
        else ->
            if character already in counter -> increment counter, move right border by 1
            else it's mean we have unique character ->
                if adding this character exceed limit (len(counter) + 1 > k) -> move window
                else -> add to cunter, move right border by 1
    5. To move window
        1. decrement character by left pointer in counter.
            if counter for char is 0 -> remove from counter
        2. add right symbol (if exist increment if not -> 1)
        move left and right pointer by 1
    """
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        if k >= len(s):
            return len(s)
        counter = {}  # store str->count
        # assighn first window
        for i in range(k):
            counter[s[i]] = counter.get(s[i], 0) + 1
        
        left = 0
        right = k

        # if new char exceed limit -> move window
        # if window limit already exceeded -> move window
        def move_counter(left, right):
            left_char_count = counter[s[left]]  # decrease counter, if less 1, pop out
            if left_char_count > 1:
                counter[s[left]] -= 1
            else:
                counter.pop(s[left])
            counter[s[right]] = counter.get(s[right], 0) + 1

        while right < len(s):
            if len(counter) > k:  # we exceeding k limit and have to move window right
                move_counter(left, right)
                left += 1
                right += 1
            else:
                if s[right] in counter:
                    counter[s[right]] += 1
                    right += 1
                else:  # new unique symbol
                    if len(counter) + 1 > k: # we about to exceed k limit
                        move_counter(left, right)
                        left += 1
                        right += 1
                    else:
                        counter[s[right]] = 1
                        right += 1
        return right - left # return window size



if __name__ == '__main__':
    n = "eceba" # 3
    k = 2
    # n = 'abacae' # 5
    # k = 3
    n = 'xyxyaaabb' # 5
    k = 2
    # n = 'aa'
    # k = 1
    # n = "ababffzzeee" # 5
    # k = 2
    sol = Solution()
    res = sol.lengthOfLongestSubstringKDistinct(n, k)
    print(f'Result --> {res}')  