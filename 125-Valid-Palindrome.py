class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        alphanumeric = "0123456789abcdefghijklmnopqrstuvwxyz"

        while l < r:
            if s[l].lower() not in alphanumeric:
                l +=1
            elif s[r].lower() not in alphanumeric:
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l +=1
                r -=1
        return True
