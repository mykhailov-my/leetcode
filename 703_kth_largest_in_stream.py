import heapq

class KthLargest:
    """
    Status -> Implemented with solution

    Tags -> Heap

    Time complexity ->
    Space complexity ->

    Solution
    1.
    2.
    3.

    Notes 
    """
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

if __name__ == '__main__':
    sol = KthLargest(3, [4, 5, 8, 2])
    print(sol.add(3)) # 4
    print(sol.add(5)) # 5
    print(sol.add(10)) # 5
    print(sol.add(9)) # 8
    print(sol.add(4)) # 8
    # print(f'Result --> {res}')  