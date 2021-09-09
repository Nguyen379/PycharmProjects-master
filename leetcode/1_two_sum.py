from typing import List


class Brute:
    def twoSum(self, nums: List[int], target: int) -> List[int, int]:
        for n in range(len(nums)):
            tg = target
            tg -= nums[n]
            for m in range(n, len(nums)):
                if nums[m] == tg:
                    return [n, m]
                else:
                    pass
# Time complexity: O(n^2), Space complexity: O(1)


class One_pass_hash_table:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for idx, x in enumerate(nums):
            if target - x in dct:
                return [idx, dct[target - x]]
            else:
                dct[x] = idx
# Time complexity: O(n), Space complexity: O(n)


class Two_pass_hash_table:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for idx, x in enumerate(nums):
            dct[x] = idx
        for idx, x in enumerate(nums):
            if target-x in dct:
                return [idx, dct[target-x]]
