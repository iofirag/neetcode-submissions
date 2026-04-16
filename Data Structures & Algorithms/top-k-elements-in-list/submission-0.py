class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
            
        counters = {}

        for num in nums:
            if num not in counters:
                counters[num] = 0
            counters[num] += 1

        sorted_keys = sorted(counters, key=counters.get, reverse=True)
        
        return sorted_keys[:k]

        