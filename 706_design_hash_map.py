
class MyHashMap:
    """
    Status -> Solved by myself

    def put(self, key: int, value: int) -> None:
        Time complexity -> O(N)
        Space complexity -> O(N)

        Solution
        1. look if key exist, if yes -> update it
        2. if not, add it, increase size
        3. if size out of limit -> scale up
            3.1 allocate new list
            3.2 hash old values into new map
    
    def get(self, key: int) -> int:
        Time complexity -> O(N)
        Space complexity -> O(N)

        Solution
        1. get hash, iterate by list looking for a key, if no key -> return -1
    
    def remove(self, key: int) -> None:
        Time complexity -> O(N)
        Space complexity -> O(N)

        Solution:
        1. find in nested list key, put back element into i-th, pop last

    """

    def __init__(self):
        self.allocated = 4
        self.fill_factor = 0.75
        self.list = [list() for i in range(self.allocated)]
        self.len = 0

    def hash(self, key):
        return key % self.allocated

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        _updated = False
        for i in range(len(self.list[h])):
            if self.list[h][i][0] == key:  # if key in map exist
                _updated = True
                self.list[h][i][1] = value

                break
        if not _updated:  # that a new key, add it to back
            self.list[h].append([key, value])
            self.len += 1

        if self.len / self.allocated > self.fill_factor:  # size up
            k = 2
            self.allocated *= k
            new_list = [list() for i in range(self.allocated)]
            for line in self.list:
                for k, v in line:
                    new_list[self.hash(k)].append([k, v])
            self.list = new_list


    def get(self, key: int) -> int:
        for k, v in self.list[self.hash(key)]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        for i in range(len(self.list[h])):
            if self.list[h][i][0] == key:  # if key in map exist
                self.list[h][i] = self.list[h][-1]
                self.list[h].pop()
                break



if __name__ == '__main__':
    m = MyHashMap()
    m.put(1, 1)
    assert m.get(1) == 1
    m.put(40, 40)
    assert m.get(40) == 40
    m.put(1, 123)
    assert m.get(1) == 123
    m.put(2, 2)
    m.put(3, 2)
    m.put(4, 4)
    # print(m.get(1))
    assert m.get(1) == 123
    m.remove(1)
    # print(m.get(1))
    # print(f'Result --> {res}')
    m = MyHashMap()
    m.put(1, 1)
    m.remove(1)