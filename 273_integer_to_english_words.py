"""
Status -> Solved by myself

Time complexity -> O(N)
Space complexity -> O(log N)

Solution
0. Create mapper of 1 to 20, then step by 10 to 100
1. divide number to three digit batches
2. Each batch has suffix ('Billion', 'Million', 'Thousand', '')
3. resolve each batch and add suffix
4. resolve 3 digit
    0. if any digit is zero do not add anything to list
    1. find amount of hundreds and add to list {digit} Hundred
    2 go to next two digits, if they are <= then 20 -> add to list from mapper
    3 else add to list first digit multiplied by 10 (20, 30, 40 etc) from mapper
    4. add to list third digit from mapper
5. combine all from list to string
"""

class Solution:

    num_map = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
        100: 'Hundred',
    }
    def resolve_hundred(self, n):
        # return list of words for 0 <= n <= 999
        words = []
        hundreds = n // 100
        if hundreds > 0:
            words.append(self.num_map[hundreds])
            words.append(self.num_map[100])
        dozens = n % 100
        if dozens <= 20 and dozens > 0:
            words.append(self.num_map[dozens])
        else:
            first_digit = self.num_map.get((dozens // 10) * 10)
            if first_digit:
                words.append(first_digit)
            second_digit = self.num_map.get(dozens % 10)
            if second_digit:
                words.append(second_digit)
        return words


    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        n = num
        num_batches = []
        for i in [1000000000, 1000000, 1000, 1]:
            num_batches.append(n // i)
            n = n % i
        words = []
        for batch, suffix in zip(num_batches, ['Billion', 'Million', 'Thousand', '']):
            if batch == 0:
                continue
            words.extend(self.resolve_hundred(batch))
            if suffix:
                words.append(suffix)
        return " ".join(words)




if __name__ == '__main__':
    n = 100000
    sol = Solution()
    res = sol.numberToWords(n)
    print(f'Result --> {res}')  