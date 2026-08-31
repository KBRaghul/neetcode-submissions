class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            min_value = min(heights[left], heights[right])
            area = min_value * (right - left)

            max_area = max(area,max_area)
            if(min_value == heights[left]):
                left += 1
            else:
                right -= 1

        return max_area    

        
