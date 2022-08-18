from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        print(arr)
        c = Counter(arr)
        print(c)
        # 12312322
        # 1: 2, 2: 4, 3: 2
        # len = 8
        cc = [[k,v] for k,v in c.items()]
        print(cc)
        cc.sort(key=lambda x: -x[1])
        print(cc)
        half = len(arr) // 2
        acc = 0
        for i in range(len(cc)):
            print(i, acc, half)
            if acc >= half:
                print(i)
                return i
            acc += cc[i][1]
        return len(cc)