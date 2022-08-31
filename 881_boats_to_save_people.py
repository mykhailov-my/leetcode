
from bisect import bisect_left


class Solution:
    """
    Status -> Not working

    Tags -> bisearch, sorting

    Time complexity -> O(N Log N)
    Space complexity -> O(N)

    """
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        saved_people = set()
        used_boats = 0
        for i in range(len(people)):
            if i in saved_people:
                continue
            space_left = limit
            for _ in range(2):
                j = bisect_left(people, space_left)
                if j == len(people):
                    j -= 1
                # breakpoint()
                if j in saved_people:
                    # if j in saved_people we iterate to right as long as it's a same number
                    j_copy = j
                    while j_copy < len(people) and people[j_copy] == people[j] and j_copy in saved_people:
                        j_copy += 1
                    breakpoint()
                    if people[j_copy] != people[j]:
                        # breakpoint()
                        if space_left < limit:
                            used_boats += 1
                            break
                    else:
                        j = j_copy

                    
                if people[j] <= space_left:
                    saved_people.add(j)
                    space_left -= people[j]
                    if _ == 1 and space_left < limit:
                        used_boats += 1
                elif people[j - 1] > space_left and space_left < limit:
                    used_boats += 1
                    break
        return used_boats


class Solution2:
    """
    Status -> Solved by myself

    Tags -> Sorting, two pointers

    Time complexity -> O(N log N)
    Space complexity -> O(1)

    Solution
    1. sort array
    2. init left, right
    3. while left <= right, <= cos if final pair exceed limit we have to put each of them on boat and one iteration more needed
    4. if sum exceed limit -> we put on boat only men on right, so we move only right pointer, increase boats num
    5. else -> move both pointers and increase boat num

    Notes 
    """
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] > limit:
                boats += 1
                right -= 1
            else:
                boats += 1
                right -= 1
                left += 1
        return boats
        

if __name__ == '__main__':
    n = [3,2,2,1]  # 3
    l = 3
    n = [1,2]
    l = 3
    n = [3,5,3,4]
    l = 4
    sol = Solution2()
    res = sol.numRescueBoats(n, l)
    print(f'Result --> {res}')  