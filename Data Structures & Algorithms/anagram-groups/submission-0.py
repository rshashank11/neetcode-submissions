class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        anagrams_hash = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if anagrams_hash.get(sorted_str):
                anagrams_hash[sorted_str].append(str)
            else:
                anagrams_hash[sorted_str] = [str]
        
        for ele in anagrams_hash:
            anagrams.append(anagrams_hash[ele])
        
        return anagrams