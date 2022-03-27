
bad = 15
def isBadVersion(version: int) -> bool:
    print(f'Version check {version} is_bad {version >= bad } ')
    return version >= bad 

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def recursive_search(start_version: int, last_version: int):
            if start_version == last_version:
                return start_version if isBadVersion(start_version) else None
            else:
                range_middle = round((last_version - start_version) / 2) + start_version
                if isBadVersion(range_middle):
                    return recursive_search(start_version, range_middle)
                else:
                    return recursive_search(range_middle + 1, last_version)
        return recursive_search(1, n)

if __name__ == '__main__':
    n = 145
    sol = Solution()
    res = sol.firstBadVersion(n)
    print(f'Result --> {res}')
    