"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""

class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.d = {}
        for i, word in enumerate(wordsDict):
            indices = self.d.get(word, [])
            indices.append(i)
            self.d[word] = indices
    
    def closest_nums(self, arr1, arr2):
        smallest = float('inf')
        for n1 in arr1:
            for n2 in arr2:
                smallest = min(abs(n1-n2), smallest)
        return smallest

    def shortest(self, word1: str, word2: str) -> int:
        return self.closest_nums(self.d[word1], self.d[word2])


if __name__ == '__main__':
    wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    _ = wd.shortest("makes", "coding")
    print(_)
    # sol = Solution()
    # res = sol.func(n)
    # print(f'Result --> {res}')  