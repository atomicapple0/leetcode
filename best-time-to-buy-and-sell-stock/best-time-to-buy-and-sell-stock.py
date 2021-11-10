class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find diff between lowest price and the subsequent highest price that is seen after
        lowest_so_far = prices[0]
        best = 0
        for p in prices[1:]:
            sell_now = p - lowest_so_far
            best = max(best, sell_now)
            lowest_so_far = min(lowest_so_far, p)
        return best
        