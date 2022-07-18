"""
Status -> Solved by myself
Time complexity -> O(N + M)
Space complexity -> O(N + M)

Solution
1. create dict to count how much each number occurs
2. iterate by one of the dict
3. if key exist in second dict -> add to result list of keys repeated minimum amount of times
"""

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def count_values(l):
            counter = {}
            for val in l:
                counter[val] = counter.get(val, 0) + 1
            return counter
        
        counter_1 = count_values(nums1)
        counter_2 = count_values(nums2)
        result = []
        for key in counter_1:
            if key in counter_2:
                result.extend([key for amount in range(min(counter_1[key], counter_2[key]))])
        return result


if __name__ == '__main__':
    n = [4,9,5]
    m = [9,4,9,8,4]
    sol = Solution()
    res = sol.intersect(n, m)
    print(f'Result --> {res}')  