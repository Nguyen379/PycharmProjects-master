class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
        return res

    def helper(self, s, l, r):
        while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
        return s[l + 1:r]

        # while 0 <= l and r < len(s):
        #     if s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     else:
        #         break
        # return s[l + 1:r]


print(Solution().longestPalindrome("cbbd"))
