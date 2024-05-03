class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexes = {}
        for i, num in enumerate(nums):
            difference = target - num
            
            if difference in indexes:
                return([i, indexes[difference]])
            
            indexes[num] = i
