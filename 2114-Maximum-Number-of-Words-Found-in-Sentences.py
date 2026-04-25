class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        out = 0
        for i in sentences:
            out = max(out, len(i.split()))
        return out
