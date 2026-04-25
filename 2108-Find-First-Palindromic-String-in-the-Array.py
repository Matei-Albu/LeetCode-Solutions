class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        status = True
        for i in words:
            l,r = 0, len(i) - 1
            while l <= r:
                if i[l] == i[r]:
                    l += 1
                    r -= 1
                    status = True
                else:
                    status = False
                    break
            if status:
                return i
        return ""

            
