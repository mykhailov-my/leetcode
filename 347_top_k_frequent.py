# Done with help
from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = defaultdict(list)
        biggest = 0
        for num, count in Counter(nums).items():
            frequency[count].append(num)
            biggest = max(biggest, count)
            
        result = []
        for count in range(biggest, 0, -1):
            result.extend(frequency[count])
            if len(result) == k:
                return result
        return result[:k]

if __name__ == '__main__':
    nums = [1,2,3]
    k = 2
    sol = Solution()
    res = sol.topKFrequent(nums, k)
    print(f'Result --> {res}')