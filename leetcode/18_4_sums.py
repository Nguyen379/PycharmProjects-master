class Solution:
    def fourSum(self, nums, target):
        output = []
        nums = sorted(nums)
        for x in range(len(nums) - 3):
            if x != 0 and nums[x] == nums[x - 1]:
                continue
            for y in range(x + 1, len(nums) - 2):
                if nums[y] == nums[y - 1] and y != x+1:
                    continue
                z, t = y + 1, len(nums) - 1
                while z < t:
                    total = nums[x] + nums[y] + nums[z] + nums[t]
                    if total == target:
                        output.append([nums[x], nums[y], nums[z], nums[t]])
                        while z < t and nums[z] == nums[z + 1]:
                            z += 1
                        while z < t and nums[t] == nums[t - 1]:
                            t -= 1
                        z += 1
                        t -= 1
                    elif total < target:
                        z += 1
                    else:
                        t -= 1
        return output

    def fourSum2(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

    def fourSum3(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results


print(Solution().fourSum([-2, -1, -1, 1, 1, 2, 2], 0))
# [[-2, -1, 1, 2], [-2, -1, 1, 2], [-1, -1, 1, 1]]
print(Solution().fourSum([2, 2, 2, 2, 2], 8))
# [[2,2,2,2]]
print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
# [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
