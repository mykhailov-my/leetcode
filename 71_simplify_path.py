"""
Status -> Solved by myself

Time complexity -> O(N)
Space complexity -> O(N)

Solution
1.create list, left pointer assign to 1, add to end slash since we do operation on slashes
2. iterate by string from 1, if slash ->
3. if [left:i] is slash or dot -> it's garbage, move left pointer above them (i + 1)
4. if two dots -> move left pointer and pop from list if possible
5. else move left pointer, and if it's non empty string add to list
6. return string from list separeted by /
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        left = 1
        result = []
        path += '/'
        for i in range(1, len(path)):
            if path[i] == '/':
                # print(path[left:i])
                if path[left:i] == '/' or path[left:i] == '.':
                    left = i + 1
                    continue
                elif path[left:i] == '..':
                    left = i + 1
                    if len(result) >= 1:
                        result.pop()
                    continue
                else:
                    if path[left:i] != '':
                        result.append(path[left:i])
                    left = i + 1
        # print(result)
        return "/" + "/".join(result,)

"""
Time complexity -> O(N)
Space complexity -> O(N)

Solution
1. create list
2. iterate over split string by /
3. if p is empty or . -> continue
4. if .. and list not empty -> pop out
5. else append to list
6. return string from list separeted by /
"""

class Solution2:
    def simplifyPath(self, path: str) -> str:
        res = []
        for p in path.split('/'):
            # print(p)
            if p == '' or p == '.':
                continue
            elif p == '..':
                if len(res) > 0:
                    res.pop()
                continue
            else:
                res.append(p)
        return "/" + "/".join(res,)

if __name__ == '__main__':
    n = "//home//foo/././....//"
    n = "/../"
    # n = "/a//b////c/d//././/.."
    n = "/a/./b/../../c/"

    sol = Solution2()
    res = sol.simplifyPath(n)
    print(f'Result --> {res}')  