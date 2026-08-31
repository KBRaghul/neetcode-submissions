class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for ind, num in enumerate(nums):

            if num > 0:
                break

            if ind > 0 and nums[ind - 1] == num:
                continue
            
            l = ind + 1
            r = len(nums) - 1

            while l < r:
                threeSum = num + nums[r] + nums[l]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                


        return result
            

