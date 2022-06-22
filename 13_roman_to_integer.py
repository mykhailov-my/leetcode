"""
Status -> Solved by myself

Time complexity -> O(n)
Space complexity -> O(1)

Solution
1. Have  symbol translation dict
2. if on right symbol with bigger value -> substract value from total amount
3. else add value to total
"""

class Solution:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        amount = 0
        for i, num in enumerate(s):
            value = self.roman_values[num]
            if i + 1 < len(s) and self.roman_values[s[i + 1]] > value:
                amount -= value
            else:
                amount += value
        return amount



if __name__ == '__main__':
    n = "MCMXCIV"
    sol = Solution()
    res = sol.romanToInt(n)
    print(f'Result --> {res}')  