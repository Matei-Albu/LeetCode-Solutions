class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            length = min(height[l], height[r])

            if length* (r-l)> area:
                area = length*(r - l)
            
            if height[r] > height[l]:
                l +=1
            else:
                r-=1
        return area
