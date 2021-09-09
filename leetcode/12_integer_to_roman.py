class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        output = ""
        for idx, x in enumerate(nums):
            output += num//x * rom[idx]
            num = num%x
        return output
