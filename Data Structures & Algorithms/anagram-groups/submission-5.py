class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        total_strs = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            total_strs[sorted_s].append(s)
        return list(total_strs.values())    