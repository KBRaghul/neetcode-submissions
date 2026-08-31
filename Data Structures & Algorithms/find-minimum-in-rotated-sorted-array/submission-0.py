class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = nums[0]

        for n in nums:
            min_value = min(min_value, n)
            
        return min_value
        