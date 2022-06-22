"""
Status -> Implemented with solutio

Time complexity -> O(n)
Space complexity -> O(1)

Solution
1. start from end of list
2. check if we can reach to last index, (Sum of index and nums[index] have to bigger or eq last index) - > put new last index
3. check if last index is 0
"""

# class Solution:
#     def canJump(self, nums: list[int], index=0) -> bool:
#         # check if we can  jump to the end right now
#         # find nuber that allow to jump max distance
#         # if max distance < end -> return False
#         jump_len = nums[index]
#         if jump_len + index >= len(nums):
#             return True
#         next_max_jump_index = index + 1
#         for i in range(1, jump_len):
#             breakpoint()
#             if nums[next_max_jump_index] < nums[index + i] - i:
#                 next_max_jump_index = index + i
#         if next_max_jump_index == index: 
#             return False
#         else:
#             return self.canJump(nums, index=next_max_jump_index)


class BestSolution:
    def canJump(self, nums: list[int]) -> bool:
        last_ind = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_ind:
                last_ind = i
        return last_ind == 0

if __name__ == '__main__':
    n = [2,3,1,1,4]
    # n = [3, 5, 0 ,2, 0, 0, 1]
    # n = [3,2,1,0,4]
    # n = [5, 0, 666]
    sol = BestSolution()
    res = sol.canJump(n)
    print(f'Result --> {res}')  