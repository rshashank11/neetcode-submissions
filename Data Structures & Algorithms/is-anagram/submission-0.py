class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash = {}
        t_hash = {}
        for char in s:
            if s_hash.get(char):
                s_hash[char] = s_hash[char] + 1
            else:
                s_hash[char] = 1
        
        for char in t:
            if t_hash.get(char):
                t_hash[char] = t_hash[char] + 1
            else:
                t_hash[char] = 1

        for char in s:
            if s_hash.get(char) == t_hash.get(char):
                continue
            else:
                return False

        return True