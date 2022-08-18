class Solution:
    def fact(self, x):
        if x == 0:
            return 1
        return x * self.fact(x-1)
    
    def nCr(self, n, r):
        return self.fact(n) / self.fact(n - r) / self.fact(r)
    def uniquePaths(self, m: int, n: int) -> int:
        # m + n C n
        return int(self.nCr(m+n-2, n-1))