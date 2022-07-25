"""
Status -> Solved by myself

Time complexity -> O(1)
Space complexity -> O(unique messages)

Solution
1. create dict msg -> ts
2. get existing ts for msg
3. if no msg -> store msg -> ts to dict, return true
4. else if ts exist ->
5. if current ts >= existing ts -> update dict, return True
6. else -> return False 
"""

class Logger:
    msg_mapper = {}

    def __init__(self):
        self.msg_mapper = {}

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
    