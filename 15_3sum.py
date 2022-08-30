"""
Status -> Implemented with solution

Time complexity ->
Space complexity ->

Solution
1. initate hash map for result, duplicates for val1 and dict seen
2. iterate by nums for first value
3. if first value not in duplicates hash ->
4. add value to duplicates
5. Iterate by nums starting from next position from val1
6. complement = -val1 - val2 (v1 + v2 + v3 = 0| -v3 = v1 + v2| v3 = -v1 -v2) (it's a value that we're looking for)
7. If complement in seen and seen[complement] == i -> add to result sorted tuple of val1, val2 and complement
8. add to dict val2 -> index of val1
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for val2 in nums[i+1:]:
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res


class Solution2:
    '''
    Brute force, too slow
    '''
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_map = {}
        for i in range(len(nums)):
            l = nums_map.get(nums[i], [])
            l.append(i)
            nums_map[nums[i]] = l
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        print(i,j,k)
                        result.add(tuple(sorted((nums[i],nums[j],nums[k]))))
        return result


class Solution3:
    '''
    Time complexity -> O(N^2)
    Space complexity -> O(N)

    Acceptable solution but too slow
    '''
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_map = {}
        for i in range(len(nums)):
            l = nums_map.get(nums[i], [])
            l.append(i)
            nums_map[nums[i]] = l
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if -nums[i] -nums[j] in nums_map:
                    indices = nums_map[-nums[i] -nums[j]]
                    if (len(indices) > 2 or (i not in indices and j not in indices)):
                        result.add(tuple(sorted((nums[i], nums[j], nums[indices[0]]))))

        return result


class Solution4:
    '''
    Time complexity -> O(N^2)
    Space complexity -> O(N)

    Acceptable solution but too slow, slight optimization of sol3
    '''
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_map = {}
        for i in range(len(nums)):
            l = nums_map.get(nums[i], set())
            l.add(i)
            nums_map[nums[i]] = l
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if -nums[i] -nums[j] in nums_map:
                    indices = nums_map[-nums[i] -nums[j]]
                    if (len(indices) > 2 or (i not in indices and j not in indices)):
                        print(f'{i} {j} ')
                        result.add(tuple(sorted((nums[i], nums[j], -nums[i] -nums[j]))))

        return result

if __name__ == '__main__':
    n = [-1,0,1,2,-1,-4]  # [[-1,-1,2],[-1,0,1]]
    n = [-1,0,1,0]  # [[-1,0,1]]
    sol = Solution4()
    res = sol.threeSum(n)
    print(f'Result --> {res}')  