

class Solution:
    """
    Status -> Solved with hint

    Time complexity -> O(N)
    Space complexity -> O(1)

    Solution
    1. init left, right and zero counter
    2. init window
    3. iterate by nums
        if new symbol is 0 ->
            if we at limit or more (zero_counter >= k) -> move window, update counter
            else -> expand window
        else ->
            if we exceeded limit means we have more zeros then allowed and we can't add another 1
            -> move window
            else -> expand window
    4. return window size
    """
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        right = k
        zero_counter = 0

        for i in range(k):
            if nums[i] == 0:
                zero_counter += 1
        
        while right < len(nums):
            if nums[right] == 0:
                if zero_counter >= k:  # move window
                    if nums[left] == 0:
                        zero_counter -= 1
                    zero_counter += 1
                    left += 1
                    right += 1
                else:
                    zero_counter += 1
                    right += 1
            else:
                if zero_counter > k: # window is invalid and we have to move it
                    if nums[left] == 0:
                        zero_counter -= 1
                    left += 1
                    right += 1
                else:
                    right += 1
        return right - left
        # if new symbol is 0 and limit about or already exceeded -> move window
        # if new symbol is 0 and limit not exceeded -> move right pointer
        # if symbol is 1 and we at limit (zero counter == k) -> move right pointer
        # if symbol is 1 and we exceeded limit -> move window
        pass

class BetterSolution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        zero_counter = 0
        ans = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_counter += 1
            while zero_counter > k:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans

if __name__ == '__main__':
    n = [1,1,1,0,0,0,1,1,1,1,0] #6
    k = 2
    n = [1,0,0,1,1,0,0,1,1,0,0,0,1,1,1] # 6
    k = 2
    n = [1,0]
    k = 1
    sol = Solution()
    res = sol.longestOnes(n, k)
    print(f'Result --> {res}')  