class Solution:
    def posPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        c = self.posPow(x,n//2)
        return c * c * self.posPow(x,n%2)
        
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.posPow(x,-n)
        return self.posPow(x,n)

        