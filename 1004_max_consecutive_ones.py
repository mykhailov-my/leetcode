"""
Status -> Solved with hint

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""

class Solution:
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