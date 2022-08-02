"""
Status -> Implemented with solution

Time complexity -> O(1)
Space complexity -> O(1)

Solution
__init__
1. init dict and list
insert
2. if val in dict -> return False
3. add to dict val -> last index of list
4. append val to list
remove
5. if value not in dict -> return False
6. get last element, index of val
7. swap last list element with val (push element to back of the list)
8. assign index of last element to index of val
9. list.pop, dict.pop
10 return True
getRandom
11. retun random.choice(list)
"""
from collections import Counter
from random import choice


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_element, idx = self.list[-1], self.dict[val]
        self.list[idx], self.dict[last_element] = last_element, idx
        # delete the last element
        self.list.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.list)
        # rnd = randint(0, len(self.dict))



if __name__ == '__main__':
    # n = ...
    rs = RandomizedSet()
    # _ = rs.remove(1) # False
    # print(_)
    _ = rs.insert(1) # True
    print(_)
    _ = rs.getRandom() # 1
    print(_)
    _ = rs.remove(1) # True
    print(_)
    _ = rs.insert(1) # True
    print(_)

    # _ = rs.insert(2) # True
    # print(_)
    # _ = rs.insert(3) # True
    # print(_)
    # _ = rs.insert(2) # False
    # print(_)
    # _ = Counter([rs.getRandom() for i in range(100)])
    # print(_)
    # _ = rs.remove(4) # False
    # print(_)
    # _ = rs.remove(3) # True
    # print(_)
    # _ = Counter([rs.getRandom() for i in range(100)])
    # print(_)
    # print(f'Result --> {res}')  