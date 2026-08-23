class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_nums = set(nums)
        highest = 0

        for n in my_nums:
            if (n - 1) not in my_nums:
                length = 1
                while (n + length) in my_nums:
                    length += 1
                
                if length > highest:
                    highest = length

        return highest

