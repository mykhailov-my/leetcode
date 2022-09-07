
class Solution:
    """
    Status -> WIP

    Tags ->

    Time complexity ->
    Space complexity ->


    Notes 
    It's seems there possible solution with O(1) memory, but most likely may have time complexity more then O(N)
    """
    def calPoints(self, ops: list[str]) -> int:
        if len(ops) == 1:
            return int(ops[0])
        ptr = 1
        result_sum = ops[0]
        while ptr < len(ops):
            if ops[ptr] == '+':
                sum_ = int(ops[ptr-1]) + int(ops[ptr-2])
                result_sum += sum_
                ops[ptr] = sum_
            elif ops[ptr] == 'C':
                result_sum -= int(ops[ptr-1])
            elif ops[ptr] == 'D':
                pass
            else:
                result_sum += int(ops[ptr])
            ptr += 1
        return result_sum

['1', '2', '3', 'C', 'C']
['0', '0', '1', '2', 'C']
['0', '0', '0', '0', '1']

['1', 'C']
['0', '0']

['5', '1', '2', '3', 'C', 'C', '+']
['5', '0', '0', '1', '2', 'C', '+']
['5', '0', '0', '0', '0', '1', '+']


class Solution2:
    """
    Status -> Solved by myself

    Tags -> stack

    Time complexity -> O(N)
    Space complexity -> O(N)

    Notes 
    Obvious solution
    """
    def calPoints(self, ops: list[str]) -> int:
        result_sum = 0
        queue = list()
        for symbol in ops:
            if symbol == '+':
                queue.append(queue[-1] + queue[-2])
                result_sum += queue[-1]
            elif symbol == 'C':
                result_sum -= queue.pop()
            elif symbol == 'D':
                queue.append(queue[-1] * 2)
                result_sum += queue[-1]
            else:
                queue.append(int(symbol))
                result_sum += queue[-1]
        return result_sum


if __name__ == '__main__':
    n = ["5","-2","4","C","D","9","+","+"] # 27
    # n = ['1', '1', '1', 'C', 'C']
    sol = Solution2()
    res = sol.calPoints(n)
    print(f'Result --> {res}')  