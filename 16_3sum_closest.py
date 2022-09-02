

class Solution:
    """
    Status -> Implemented with solution

    Tags -> Sorting, 2 pointer

    Time complexity -> O(N^2)
    Space complexity -> O(1)

    Solution
    1. sort nums
    2. initiate first closest sum
    3. iterate from 0 to end - 1 nums included (range(len(nums) - 2))
        4. initiate second pointer as i + 1
        5.  third pointer is nums end
        6. iterate while second pointer less then third
            7. calculate new sum
            8. if current sum equal target -> job is done
            9. check if current sum closer then closest_sum and update if needed
            10. ifcurrent sum less then needed -> increment second counter
            11. else -> right pointer increment
    12 return closest sum

    Notes 
    """
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == target:
                    return target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    j += 1
                else:
                    k-= 1
        return closest_sum

            



if __name__ == '__main__':
    n = [-1,2,1,-4] # 2
    t = 1
    n = [0,0,0]
    t = 1
    n = [4,0,5,-5,3,3,0,-4,-5]
    t = -2

    sol = Solution()
    res = sol.threeSumClosest(n, t)
    print(f'Result --> {res}')  