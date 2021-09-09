class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
               "V": 5, "IV": 4, "I": 1}
        output = 0
        for n in range(len(s)):
            if n < len(s) - 1 and s[n:n + 2] in rom:
                continue
            elif n > 0 and s[n - 1:n + 1] in rom:
                output += rom[s[n - 1:n + 1]]
            else:
                output += rom[s[n]]
        return output

    def romanToInt2(self, s: str) -> int:
        res, prev = 0, 0
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in s[::-1]:  # rev the s
            if dict[i] >= prev:
                res += dict[i]  # sum the value iff previous value same or more
            else:
                res -= dict[i]  # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
            prev = dict[i]
        return res


print(Solution().romanToInt("IV"))
