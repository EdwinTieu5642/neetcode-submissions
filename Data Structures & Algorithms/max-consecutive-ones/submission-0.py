class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        count = 0
        for i in nums:
            if i == 1:
                count = count + 1
                if count > max_one:
                    max_one = count
            elif i == 0:
                count = 0
        return max_one