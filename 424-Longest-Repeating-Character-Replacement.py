class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0

        res = 0
        maxchar = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord("A")] += 1
            maxchar = max(maxchar,  count[ord(s[r]) - ord("A")]) 

            while (r - l + 1) - maxchar > k:   
                count[ord(s[l]) - ord("A")] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res
