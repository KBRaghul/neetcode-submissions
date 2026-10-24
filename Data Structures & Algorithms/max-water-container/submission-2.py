class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0

        while l < r:
            min_value = min(heights[l], heights[r])
            curr_area = min_value * (r-l)

            area = max(area, curr_area)
            if min_value == heights[l]:
                l += 1
            else:
                r -= 1
        
        return area
            
        