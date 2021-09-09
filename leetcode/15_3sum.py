class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        output = []
        for x in range(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                # nums[x-1] because nums[x] == nums[y] happens twice in [1, 1, 1]
                # nums[x+1] will skip all 1 until last => losing one pair
                continue
            y, z = x + 1, len(nums) - 1
            while y < z:
                total = nums[x] + nums[y] + nums[z]
                if total > 0:
                    z -= 1
                elif total < 0:
                    y += 1
                else:
                    output.append([nums[x], nums[y], nums[z]])
                    while y < z and nums[y] == nums[y + 1]:
                        y += 1
                    while y < z and nums[z] == nums[z - 1]:
                        z -= 1
                    y += 1
                    z -= 1
        return output


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
# -4 -1 -1 0 1 2
