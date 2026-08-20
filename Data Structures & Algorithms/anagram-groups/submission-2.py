class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       from collections import defaultdict
       dict_sorted = defaultdict(list)
       for s in strs:
        sorteds = "".join(sorted(s))
        dict_sorted[sorteds].append(s)
       return list(dict_sorted.values())