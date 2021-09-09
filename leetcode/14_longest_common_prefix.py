class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        shortest_word = min(strs, key=len)
        # min(strs) return lowest word alphabetically
        for idx, x in enumerate(shortest_word):
            for str in strs:
                if str[idx] != x:
                    return shortest_word[:idx]
        return shortest_word


print(Solution().longestCommonPrefix([""]))
