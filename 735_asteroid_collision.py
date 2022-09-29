
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
    # def asteroidCollision(self, asteroids: list[int]) -> list[int]:
    #     right_stack = []  # > 0
    #     left_stack = []  # < 0
    #     for asteroid in asteroids:
    #         if asteroid < 0:
    #             if right_stack:
    #                 if right_stack[-1] > abs(asteroid):
    #                     continue
    #                 else:
    #                     right_stack.pop()
    #             else:
    #                 left_stack.append(asteroid)
    #         else:
    #             if left_stack:
    #                 if abs(left_stack[-1]) > asteroid:
    #                     continue
    #                 else:
    #                     left_stack.pop()
    #             else:
    #                 right_stack.append(asteroid)
        
    #     return max(left_stack, right_stack)

    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = [asteroids[0]]
        # for asteroid in asteroids[1:]:
        i = 1
        while i < len(asteroids):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:  # < 0
                if stack and stack[-1] > 0:  # collision
                    if stack[-1] > abs(asteroids[i]):  # left asteroid win
                        pass
                    elif stack[-1] < abs(asteroids[i]): # right asteroid win
                        stack.pop()
                        i -= 1
                    else:  # both loose
                        stack.pop()
                else:  # no collision 
                    stack.append(asteroids[i])
            i += 1
        return stack

if __name__ == '__main__':
    n = [10,2,-5]
    n = [-2,-1,1,2]
    # n = [-2,-2,1,-2]  # [-2, -2, -2]
    # n = [10, -10]
    n = [1, -2, -2, -2]
    sol = Solution()
    res = sol.asteroidCollision(n)
    print(f'Result --> {res}')  