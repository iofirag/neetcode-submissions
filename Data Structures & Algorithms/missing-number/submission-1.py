class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for _, num in enumerate(nums):
            total = total ^ num
        for i in range(n+1):
            total = total ^ i

        return total