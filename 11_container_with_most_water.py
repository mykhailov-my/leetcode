
class Solution:
    """
    Status -> Solved by myself

    Tags -> Two pointers

    Time complexity -> O(N)
    Space complexity -> O(1)

    Solution
    1. initiate result, left and right
    2. while left < right
    3. current amount of water is size between left and right pointer multimplied by height of lesser pointer
    4. move lesser pointer, if they equal move both

    Notes 
    """
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            current_amount = (right - left) * min(height[left], height[right])
            max_water = max(max_water, current_amount)
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1
                right -= 1

        return max_water



if __name__ == '__main__':
    n = [1,8,6,2,5,4,8,3,7] # 49
    # n = [1,1,1,1] # 3
    # n = [1,4,4,1] # 4
    # n = [1,2,5,5] # 5
    # n = [0,1,2,3]
    n = [1,1]
    sol = Solution()
    res = sol.maxArea(n)
    print(f'Result --> {res}')  