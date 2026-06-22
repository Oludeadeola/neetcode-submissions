class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        num_dict = defaultdict(int)  
        for i in nums:
            num_dict[i]+=1
        for key,value in num_dict.items():
            if value >1:
                return True
        return False  

  
 
 