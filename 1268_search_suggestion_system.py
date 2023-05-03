from bisect import bisect_left


class Solution:
    """
    Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

    Tags -> Bin search, sorting, prefix

    Time complexity -> O(N log N)
    Space complexity -> O(W)
    (w - word, N - amount of products)
    Solution
    1. sort products
    2. build prefix for search, for each new letter look by bin search leftmost product
        3. iterate 3 times untill product name prefix and search prefix equal, add to suggestions list

    Notes 
    """
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        result = []
        for i in range(len(searchWord)):
            start = bisect_left(products, searchWord[:i + 1])
            suggestions = []
            for j in range(start, start + 3):
                if j < len(products) and searchWord[:i + 1] == products[j][:i + 1]:
                    suggestions.append(products[j])
                else:
                    break
            result.append(suggestions)
        return result


if __name__ == '__main__':
    p = ["mobile","mouse","moneypot","monitor","mousepad"]
    w = "mouse"
    sol = Solution()
    res = sol.suggestedProducts(p, w)
    print(f'Result --> {res}')