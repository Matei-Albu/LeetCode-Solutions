class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        maxlength = 0

        l = 0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            maxlength = max(maxlength, r - l + 1)
        return maxlength
