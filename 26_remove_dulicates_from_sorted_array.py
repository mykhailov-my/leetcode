
class Solution:
    """
    Status -> Solved with hint

    Tags -> Two pointers

    Time complexity -> O(N)
    Space complexity -> O(1)

    Solution
    1. initiate two pointers -> i for traversing list, unique_ptr to point last unique nums
    2. iterate by nums
        3. if current num not equal to last unique ->
            4. iterate unique pointer
            5. swap i with unique
    6. return unique num pointer + 1

    Notes 
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_ptr = 0
        i = 1
        while i < len(nums):
            if nums[i] != nums[unique_ptr]:
                unique_ptr += 1
                nums[i], nums[unique_ptr] = nums[unique_ptr], nums[i]
            i += 1
        return unique_ptr + 1


if __name__ == '__main__':
    n = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    res = sol.removeDuplicates(n)
    print(f'Result --> {res} | {n}')  