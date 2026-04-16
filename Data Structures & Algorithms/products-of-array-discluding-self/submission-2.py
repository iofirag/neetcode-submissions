class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # remove zero from nums list
        if len(nums) == 0:
            return []

        products = 1
        zero_indexes = set()
        for i,n in enumerate(nums):
            if n==0:
                zero_indexes.add(i)
            else:
                products *= n

        if len(zero_indexes) >1:
            return [0] * len(nums)
        elif len(zero_indexes) == 1:
            res = [0] * len(nums)
            for index in zero_indexes:
                res[index] = products
            return res
        else:
            return [int(products/n) for n in nums]

