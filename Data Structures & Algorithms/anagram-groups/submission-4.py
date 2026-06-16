class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range (len(strs)):
            key = ''.join(sorted (strs[i]))
            if key not in d:
                d[key] = []         #creating the empty list
            d[key].append(strs[i])  #adding the word to the bucket
        return list(d.values()) #to return the values of the dictionary as sublists
