"""
Status -> Solved by myself

Time complexity ->
Space complexity ->

Solution
get_right_bracket
1. have left_brackets counter (To not to use queue)
2. iterate from start point
3. if char == [ -> increment counter
4. if char == ]
    5. decrement counter
    6. if counter 0 -> return index

get_number_right
1. initate counter with start
2. iterte from start
3. if char not a numeric -> return counter
4. else increment counter

decode_substring (left, right)
1. if val in cache -> return from cache
2. initiate list, left and right num pointer, index as left
3. while index < right
4. if char is numeric -> use get_number_right to assign num pointers, update index to right_pointer
5. if char is [ 
    6. get ind of right and corresponding bracket
    7. use reccursion to get value of sub-expression
    8. get ammount from num pointers
    9. add to result list result of sub exp amount times
10. else -> add char to result list
11 convert list to string, store in cache and return it
"""



class Solution:
    def decodeString(self, s: str) -> str:
        cache = {}
        def get_right_bracket(start):
            left_brackets = 0
            for i in range(start, len(s)):
                if s[i] == '[':
                    left_brackets += 1
                elif s[i] == ']':
                    left_brackets -= 1
                    if not left_brackets:
                        return i

        def get_number_right(start):
            right = start
            for i in range(start, len(s)):
                if not s[i].isnumeric():
                    return right
                right += 1

        def decode_substring(left, right):
            if s[left: right] in cache:
                return cache[s[left: right]]
            sub_result = []
            left_num = None
            right_num = None
            ind = left
            while ind < right:
                if s[ind].isnumeric():
                    left_num = ind
                    right_num = get_number_right(ind)
                    ind = right_num
                if s[ind] == '[':
                    right_bracket = get_right_bracket(ind)
                    sub_string = decode_substring(ind + 1, right_bracket)
                    amount = int(s[left_num: right_num])
                    for _ in range(amount):
                        sub_result.append(sub_string)
                    ind = right_bracket
                else:
                    sub_result.append(s[ind])
                ind += 1
            result = ''.join(sub_result)
            cache[s[left: right]] = result
            return result
                
        result = decode_substring(0, len(s))
        return ''.join(result)


if __name__ == '__main__':
    n = "3[a2[c]]"  # "accaccacc"
    # n = '2[b]a2[b]' # bbabb
    n = 'a10[]a'
    sol = Solution()
    res = sol.decodeString(n)
    print(f'Result --> {res}')  