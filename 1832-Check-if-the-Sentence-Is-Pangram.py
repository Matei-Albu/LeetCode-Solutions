class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq = [0] * 26

        for i in sentence:
            freq[ord(i) - ord("a")] += 1
        
        for i in freq:
            if i == 0:
                return False
        return True
