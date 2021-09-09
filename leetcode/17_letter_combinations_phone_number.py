class Solution:
    def letterCombinations(self, digits):
        dct = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []
        if len(digits) == 1:
            return dct[digits]
        recur_prev = self.letterCombinations(digits[:-1])
        cur = dct[digits[-1]]
        return [r + c for r in recur_prev for c in cur]

    def letterCombinations2(self, digits):
        dct = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        cmb = [''] if digits else []
        for d in digits:
            cmb = [p + q for p in cmb for q in dct[d]]
        return cmb


print(Solution().letterCombinations("2345"))
