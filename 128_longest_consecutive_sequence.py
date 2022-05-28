# Did with help
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashed_nums = set(nums)
        longest_seq = 0
        
        for num in hashed_nums:
            if num - 1 not in hashed_nums:
                current_seq = 1
                current_num = num
                while current_num + 1 in hashed_nums:
                    current_seq += 1
                    current_num += 1
                longest_seq = max(longest_seq, current_seq)
        return longest_seq
        

if __name__ == '__main__':
    n = [100,4,200,1,3,2]
    sol = Solution()
    res = sol.longestConsecutive(n)
    print(f'Result --> {res}')