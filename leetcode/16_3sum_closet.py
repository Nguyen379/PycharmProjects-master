class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums = sorted(nums)
        value = float('-inf')
        for x in range(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            y, z = x + 1, len(nums) - 1
            while y < z:
                total = nums[x] + nums[y] + nums[z]
                if total - target == 0:
                    return total
                elif total - target < 0:
                    y += 1
                else:
                    z -= 1
                if abs(total - target) < abs(value - target):
                    value = total
        return value
