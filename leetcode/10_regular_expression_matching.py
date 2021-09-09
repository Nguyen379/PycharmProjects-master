class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        past = {}

        def Matching(i, j):
            if (i, j) in past:
                return past[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            # if (s[i] == p[j] or p[j] == ".") no parenthesis: i will keep increasing since p[j] == "."
            if j + 1 < len(p) and p[j + 1] == "*":
                past[(i, j)] = Matching(i, j + 2) or (match and Matching(i + 1, j))
                return past[(i, j)]
            # match comes before Matching(i+1,j) because Matching(infinite, j||p[j]==".") will be infinite
            if match:
                past[(i, j)] = Matching(i + 1, j + 1)
                return past[(i, j)]
            return False

        return Matching(0, 0)


print(Solution().isMatch("aa", "a"))  # f
print(Solution().isMatch("aa", "a*"))  # t
print(Solution().isMatch("ab", ".*"))  # t
print(Solution().isMatch("aab", "c*a*b"))  # t
print(Solution().isMatch("mississippi", "mis*is*p*."))  # f
print(Solution().isMatch("ab", ".*c"))  # t
