
class Solution:
    """
    Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

    Tags ->

    Time complexity ->
    Space complexity ->

    Solution
    1.
    2.
    3.

    Notes 
    """
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        rooms = []
        for interval in intervals:
            new_room_needed = True
            for room in rooms:
                # breakpoint()
                if room[-1][1] <= interval[0]:
                    print(f'{room}  {interval}')
                    room.append(interval)
                    new_room_needed = False
                    break
            if new_room_needed:
                rooms.append([interval])
        return len(rooms)


class Solution2:
    """
    Status -> Solved with hint

    Tags -> Sorting

    Time complexity -> O(N log N)
    Space complexity -> O(N)

    Solution
    1. sort intervals by start date
    2. init list of rooms, store there endtime of last meeting in this room
    3. iterate by intervals
        4. iterate by rooms
            5. if room <= start date interval -> replace nuber in room with interval end date
        6. if no room matched -> append to list end date of interval
    7. return len of rooms

    Notes impoved solution 1
    """
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        rooms = []
        for interval in intervals:
            new_room_needed = True
            for i in range(len(rooms)):
                if rooms[i] <= interval[0]:
                    rooms[i] = interval[1]
                    new_room_needed = False
                    break
            if new_room_needed:
                rooms.append(interval[1])
        return len(rooms)


if __name__ == '__main__':
    n = [[0,30],[5,10],[15,20]]
    # n = [[1,5],[8,9],[8,9]] # 2
    sol = Solution2()
    res = sol.minMeetingRooms(n)
    print(f'Result --> {res}')  