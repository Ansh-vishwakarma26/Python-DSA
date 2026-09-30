class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return int((high + 1)/2 - (low//2))
