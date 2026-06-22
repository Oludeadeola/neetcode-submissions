#hashmap project
from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_value = defaultdict(int)
        for i in nums :
            unique_value[i] += 1
        for key,value in unique_value.items():
            if value>1:
                return True
        return False     
             
        
        
        