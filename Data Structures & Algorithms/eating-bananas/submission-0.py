class Solution:
    def can_eat(self, piles: List[int], h : int, rate: int) -> bool:

        count = 0
        for n in range(0, len(piles)):
            count -= (-1 * piles[n]) // rate
        
        return count <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp = 1
        rp = max(piles)

        while lp != rp:
            mid = (lp + rp) // 2

            if self.can_eat(piles, h, mid):
                rp = mid
            else:
                lp = mid + 1

        return rp
