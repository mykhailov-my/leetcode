"""
Status -> Solved by myself

Time complexity -> O(N * log N + N)
Space complexity -> O(1)

Solution
1. Sort boxes types by second key from bigger to lower
2.  store loaded units and amount of boxes, iterate by sorted list
3. Count how much free space is lefted, if == 0 -> break
4. add to loaded boxes as much as possible
5. add to units amount of added boxes and multiply by box type
"""

class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        loaded_boxes = 0
        loaded_units = 0
        for box_amount, box_type in boxTypes:
            free_space = truckSize - loaded_boxes
            if free_space == 0:
                break
            loaded_boxes += min(free_space, box_amount)
            loaded_units += min(free_space, box_amount) * box_type
        return loaded_units
        pass



if __name__ == '__main__':
    n = [[5,10],[2,5],[4,7],[3,9], [1,1]]
    t = 10
    sol = Solution()
    res = sol.maximumUnits(n, t)
    print(f'Result --> {res}')  