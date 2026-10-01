class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        new = str(num)
        for each in new:
            if num % int(each) == 0:
                count += 1
        return count
                
        
