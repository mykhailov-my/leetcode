
from bisect import bisect_right


class MyCalendar:
    """
    Status -> Implemented with solution

    Tags -> Binary search, ordered List

    Time complexity -> O(N log N)
    Space complexity -> O(N)

    Solution
    1. if list empty -> add to list, return true
    2. get ind to place by bisect_right
    3. if left pair's (ind - 1) end time bigger then currnt start time -> return False
    4. if right pair's (ind) start time less then current time -> return False
    5. insert pait to index position, return True

    Notes 
    """
    def __init__(self):
        self.timestamps = []

    def book(self, start: int, end: int) -> bool:
        if not self.timestamps:
            self.timestamps.append((start, end))
            return True
        ind = bisect_right(self.timestamps, (start, end))
        if (ind > 0 and self.timestamps[ind-1][1] > start) or (ind < len(self.timestamps) and self.timestamps[ind][0] < end):
            return False
        self.timestamps.insert(ind, (start, end))
        return True

'''
True if 
end <= s2, and start >= e1 
'''

[10,20,20,30]
[10, 20]
[20, 30]
if __name__ == '__main__':
    cal = MyCalendar()
    _ = cal.book(10, 20)  # True
    print(_)
    _ = cal.book(15, 25)  # False
    print(_)
    _ = cal.book(20, 30)  # True
    print(_)
