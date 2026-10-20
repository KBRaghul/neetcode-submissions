class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums) - 1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]

        return result
        