class Solution:
    def addDigits(self, num: int) -> int:
        sums = num
        while len(str(sums)) > 1:
            temp = str(sums)
            sums = 0 
            for i in range(len(str(temp))):
                sums += int(temp[i])
        return sums
