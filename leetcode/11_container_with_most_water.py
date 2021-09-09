class Solution:
    def maxArea(self, height):
        output = 0
        l, r = 0, len(height) - 1
        while r != l:
            if height[l] > height[r]:
                area = height[r] * (r - l)
                r -= 1
            else:
                area = height[l] * (r - l)
                l += 1
            output = max(output, area)
        return output
