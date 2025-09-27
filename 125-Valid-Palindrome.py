class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        alphanumeric = set("abcdefghijklmnopqrstuvwxyz1234567890")

        while l < r:
            while l < r and s[r].lower() not in alphanumeric:
                r -= 1
            while l < r and s[l].lower() not in alphanumeric:
                l += 1
            if s[r].lower() != s[l].lower():
                return False
            l,r = l + 1, r - 1
        return True