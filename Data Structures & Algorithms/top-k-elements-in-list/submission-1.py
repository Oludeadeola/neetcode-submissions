class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        check_list = defaultdict(int)
        value = []
        for i in nums:
            check_list[i] +=1
        ranked = sorted(check_list.items(),key= lambda x : x[1], reverse= True)
        for i, j in ranked[:k]:
            value+=[i]
        return value   


        