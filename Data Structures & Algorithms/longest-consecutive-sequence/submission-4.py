class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sets = set(nums)
        lon = 0

        for n in sets:
            lon_count = 1
            if (n-1) in sets:
                continue
            while (n+lon_count) in sets:
                lon_count += 1
            
            lon = max(lon, lon_count)

        return lon