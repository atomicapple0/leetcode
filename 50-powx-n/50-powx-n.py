class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x,-n)
        if n == 0:
            return 1
        if n == 1:
            return x
        c = self.myPow(x,n//2)
        return c * c * self.myPow(x,n%2)
        