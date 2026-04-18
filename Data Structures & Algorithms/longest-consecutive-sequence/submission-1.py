class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numsset  = set(nums)
        maxnum = max(nums)
        minnum = min(nums)

        max_consecutive = 0
        consecutive = 0
        for i in range(minnum, maxnum+1):
            if i in numsset:
                consecutive += 1
                if max_consecutive < consecutive:
                    max_consecutive = consecutive
            else:
                if max_consecutive < consecutive:
                    max_consecutive = consecutive
                consecutive = 0
        return max_consecutive


