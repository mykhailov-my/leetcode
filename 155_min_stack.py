
class MinStack:
    """
    Status -> Solved with hint

    Tags -> Stack

    Time complexity -> O(1) for each method
    Space complexity -> O(1) for each method

    Solution
     __init__
    1. Initate two stacks. One for num, another to store tuple (latest min value, index in num stack)

    push(self, val: int) -> None:
    1. if min stack empty -> add (val, index)
    2. else -> if value less then last minimum -> add to min stack (val, index)
    3. add num to num stack

    pop(self) -> None:
    1. if index of last min item equal to last index in num stack (len - 1) -> populate from min stack
    2. populate from num stack

    top(self) -> int:
    1. return last from num stack

    getMin(self) -> int:
    1. return last from min stack

    Notes 
    """

    def __init__(self):
        self.num_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append((val, 0))
            # self.num_stack.append(val)
        else:
            if val < self.min_stack[-1][0]:
                self.min_stack.append((val, len(self.num_stack)))
        self.num_stack.append(val)

    def pop(self) -> None:
        if self.min_stack[-1][1] == len(self.num_stack) - 1:
            self.min_stack.pop()
        self.num_stack.pop()

    def top(self) -> int:
        return self.num_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]

[-2, 0, -3]
[(-2,0), (-3, 2)]
if __name__ == '__main__':
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    _  = stack.getMin()
    print(_)  # -3
    stack.pop()
    _ = stack.top()
    print(_) # 0
    _  = stack.getMin()
    print(_)  # -2