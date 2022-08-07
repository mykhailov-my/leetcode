"""
Status -> Implemented with solution

Time complexity -> O(N)
Space complexity -> O(1)

Solution
1.iniate fast and slow pointer as nums[0]
2. it erate forever
    3. fast = nums[nums[fast]]
    4. slow = nums[slow]
    5 break cycle if slow == fast
6. put slow at begin (slow = nums[0])
7. repeat but with same speed to the point where the both will be equal (slow == fast)
8 return slow or fast
"""

class Solution:
    '''
    Not working for edge-case [3,2,2,2,4]
    '''
    def findDuplicate(self, nums: list[int]) -> int:
        n = max(nums)
        n_sum = ((min(nums) + n) * n) // 2
        for num in nums:
            n_sum -= num
        res = abs(n_sum) // (len(nums) - n)
        breakpoint()
        return res if res <= n else n
        pass

class BestSolution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        print(f'T({tortoise}) H({hare})')
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            print(f'T({tortoise}) H({hare})')
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

if __name__ == '__main__':
    n = [1,3,4,2,2,2]
    n = [2,2,2,2,2]
    n = [1,4,4,2,4]
    n = [3,2,2,2,4]
    n = [2,5,9,6,9,3,8,9,7,1]
    
    sol = BestSolution()
    res = sol.findDuplicate(n)
    print(f'Result --> {res}')  