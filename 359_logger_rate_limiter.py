"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""

class Logger:
    msg_mapper = {}

    def __init__(self):
        pass

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        existing_ts = self.msg_mapper.get(message)
        if existing_ts is not None:
            if timestamp - existing_ts >= 10:
                self.msg_mapper[message] = timestamp
                return True
            else:
                return False
        else:
            self.msg_mapper[message] = timestamp
            return True




if __name__ == '__main__':
    logger = Logger()
    one = logger.shouldPrintMessage(100, "bug")
    print(one)
    two = logger.shouldPrintMessage(111, "bug")
    print(two)
    # _ = logger.shouldPrintMessage(3, "foo")
    # print(_)
    # _ = logger.shouldPrintMessage(8, "bar")
    # print(_)
    # _ = logger.shouldPrintMessage(10, "foo")
    # print(_)
    # _ = logger.shouldPrintMessage(11, "foo")
    # print(_)
    