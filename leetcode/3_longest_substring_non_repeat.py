class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len = start = 0
        for idx, x in enumerate(s):
            if x in used and start <= used[x]:
                start = used[x] + 1
            used[x] = idx
            max_len = max(max_len, idx+1-start)

        return max_len


print(Solution().lengthOfLongestSubstring("abc"))
