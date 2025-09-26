class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        count1 = [0]*26
        count2 = [0]*26

        for i in range(len(s)):
            count1[ord(s[i]) - ord("a")] += 1
            count2[ord(t[i]) - ord("a")] += 1

        if count1 == count2:
            return True
        return False