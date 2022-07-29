"""
Status -> Solved by myself

__init__
Time complexity -> O(N)
Space complexity -> O(N)

closest_nums
Time complexity -> O(N*M), where N - times first str occurs, M second str occurs
Space complexity -> O(1)

Solution
1. create dict word -> list of indidces where it occurs
2. iterate by two lists of indices
3. return smallest absolute differance 
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