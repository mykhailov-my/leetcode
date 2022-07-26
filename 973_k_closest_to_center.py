"""
Status -> Solved by myself


"""

import heapq
from math import sqrt


class Solution:
    '''
    Time complexity -> O(N log N)
    Space complexity -> O(N)

    Solution
    1. create heap list, dict distance -> [(x, y)]
    2. iterate by points
        3. distance = sqrt(x^2 + y^2)
        4. push distance to heap
        5. append to dict list of current x, y
    6. i = 0, result = []
    7. iterate from i to k (while, cos we need manual control)
        8. pop from heap list of smallest coordinates
        9. extend result with list, but not more then k
        10. add to I len of list
    11. return result
    '''
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        distance_map = {}
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heapq.heappush(heap, distance)
            distance_map[distance] = distance_map.get(distance, []) + [(x, y)]
        
        i = 0
        result = []
        while i <= k:
            distances = distance_map[heapq.heappop(heap)]
            result.extend(distances[:k - i])
            i += len(distances)
        return result


class Solution2:
    '''
    Time complexity -> O(N log N)
    Space complexity -> O(N)

    Solution
    1. Iterate by points
    2. add to heap tuple (distance, x, y) (distance is first, cos list comperison by first element)
    3. return list comprehension for k smallest in heap
    '''
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heapq.heappush(heap, (distance, x, y))
        return [(x, y) for _, x, y in heapq.nsmallest(k, heap)]


if __name__ == '__main__':
    n = [[3,3],[5,-1],[-2,4]]
    m = 2
    sol = Solution2()
    res = sol.kClosest(n, m)
    print(f'Result --> {res}')  