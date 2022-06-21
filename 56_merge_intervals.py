"""
Status -> Solved with hint

Time complexity -> O(N log N + N)
Space complexity -> O(1)

Best solution in terms of space
inefficient in terms of time

Solution
1. Sort values by smallest begin value
2. find if two pairs overlapping
3. if overlapping extract one pair
4. merge pairs
5. put it back
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            if self.is_overlapping(intervals[i], intervals[i+1]):
                l2 = intervals.pop(i)
                intervals[i] = [min(intervals[i][0], l2[0]), max(intervals[i][1], l2[1])]
                i -= 1
            i += 1
        return intervals

    def is_overlapping(self, l1, l2):
        if l1[0] <= l2[0] and l1[1] >= l2[1]:
            return True
        elif l2[0] <= l1[0] and l2[1] >= l1[1]:
            return True
        elif l1[1] >= l2[0] and l1[0] < l2[0]:
            return True
        elif l2[1] >= l1[0] and l2[0] < l1[0]: 
            return True
        return False


# Solution with better sorting
# Not working
class Solution2:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        smallest_begin = intervals[0][0]
        smallest_begin_index = 0
        for ind, pair in enumerate(intervals):
            if pair[0] < smallest_begin:
                smallest_begin = pair[0]
                smallest_begin_index = ind
        intervals[0], intervals[smallest_begin_index] = intervals[smallest_begin_index], intervals[0]
        print(intervals)
        i = 0
        while i < len(intervals) - 1:
            if self.is_overlapping(intervals[i], intervals[i+1]):
                l2 = intervals.pop(i)
                intervals[i] = [min(intervals[i][0], l2[0]), max(intervals[i][1], l2[1])]
                i -= 1
            i += 1
        return intervals

    def is_overlapping(self, l1, l2):
        if l1[0] <= l2[0] and l1[1] >= l2[1]:
            return True
        elif l2[0] <= l1[0] and l2[1] >= l1[1]:
            return True
        elif l1[1] >= l2[0] and l1[0] < l2[0]:
            return True
        elif l2[1] >= l1[0] and l2[0] < l1[0]: 
            return True
        return False


class BestSolution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    n = [[2,3],[4,5],[6,7],[8,9],[1,10]]

    sol = Solution2()
    res = sol.merge(n)
    print(f'Result --> {res}')  