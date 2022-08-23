"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Time limit exceeded
        def get_max_ind(l, r):  # get index of max num for window
            max_num_ind = l
            for i in range(l + 1, r + 1):
                if nums[i] > nums[max_num_ind]:
                    max_num_ind = i
            return max_num_ind
        if k == len(nums):
            return [max(nums)]
        if k == 1:
            return nums
        left = 0
        right = k - 1
        max_window_ind = 0
        res = []
        while right < len(nums):
            if left > max_window_ind or left == 0:
                max_window_ind = get_max_ind(left, right)
            else:
                if nums[right] > nums[max_window_ind]:
                    max_window_ind = right
            res.append(nums[max_window_ind])
            right += 1
            left += 1
        return res


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()
                
            # remove from deq indexes of all elements 
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]
        
        # build output
        for i in range(k, n):
            clean_deque(i)          
            deq.append(i)
            output.append(nums[deq[0]])
        return output


if __name__ == '__main__':
    n = [1,3,-1,-3,5,3,6,7]
    k = 3  # [3,3,5,5,6,7]
    # n = [1]
    # k = 1
    # n = [1, -1, 2]
    # n = [7,2,4]
    # k = 2
    sol = Solution()
    res = sol.maxSlidingWindow(n, k)
    print(f'Result --> {res}')  