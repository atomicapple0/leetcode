# s,t
# dicts = {'a':#a, 'b':#b, ...}
# dictt = {'a':#a, 'b':#b, ...}
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        
        for c in s:
            dict_s[c] += 1
        
        for c in t:
            dict_t[c] += 1
            
        for k in dict_s.keys():
            if dict_s[k] != dict_t[k]:
                return False
        
        for k in dict_t.keys():
            if dict_s[k] != dict_t[k]:
                return False
        
        return True
        