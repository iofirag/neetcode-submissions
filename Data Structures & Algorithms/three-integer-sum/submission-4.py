class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        res = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else: 
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
        
        tuples = [tuple(sorted(i)) for i in res]    # sort [3,1,2], [2,1,3] -> [1,2,3],[1,2,3] -> tuples: [(1,2,3),(1,2,3)]
        uniques = list(set(tuples))                  # [(1,2,3)]
        return [list(i) for i in uniques]             # [1,2,3]
            













        # # normalize (sort each inner list)
        # normalized = [tuple(sorted(x)) for x in res]
        # # remove duplicates
        # unique = list(set(normalized))
        # # convert back to list if needed
        # result = [list(x) for x in unique]
        # return result