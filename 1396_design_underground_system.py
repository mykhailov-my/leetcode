
"""
Status -> Solved by myself,

Solution
__init__ initiate two dicts 
    1 to store id -> start station, start time. 
    2 to store start and end stations and time
Time complexity -> O(1)
Space complexity -> O(1)


checkIn
store in check ins dict id -> start station, start time
Time complexity -> O(1)
Space complexity -> O(1)

checkOut
pop out of check ins dict by id and get start station and start time
get list of route times for this route by compiling station names, append to list new route time (end - start)
Time complexity -> O(1)
Space complexity -> O(1)

getAverageTime
sum all times and divide by len
Time complexity -> O(N)
Space complexity -> O(1)


"""
from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # id -> (start, time)
        self.routes_times = defaultdict(list)  # start__end -> [1,2,3]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        existing_ts = self.routes_times[f'{start_station}__{stationName}']
        existing_ts.append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route_times = self.routes_times[f'{startStation}__{endStation}']
        return sum(route_times) / len(route_times)


if __name__ == '__main__':
    usys = UndergroundSystem()
    usys.checkIn(45, "Leyton", 3)
    usys.checkIn(32, 'Paradise', 8)
    usys.checkIn(27, 'Leyton', 10)
    usys.checkOut(45, 'Waterloo', 15)
    usys.checkOut(27, 'Waterloo', 20)
    usys.checkOut(32, 'Cambridge', 22)
    _ = usys.getAverageTime("Paradise", "Cambridge")  # 14
    print(_)
    _ = usys.getAverageTime("Leyton", "Waterloo")  # 11
    print(_)
    usys.checkIn(10, "Leyton", 24)
    _ = usys.getAverageTime("Leyton", "Waterloo")  # 11
    print(_)
    usys.checkOut(10, "Waterloo", 38)
    _ = usys.getAverageTime("Leyton", "Waterloo")  # 12
    print(_)
