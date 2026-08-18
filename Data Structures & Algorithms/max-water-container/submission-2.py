class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        width = len(heights) - 1
        out = 0

        while lp < rp:
            area = min(heights[lp],heights[rp]) * width
            if area > out:
                out = area
            
            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
            
            width -= 1

        return out

        