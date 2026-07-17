#from collections import defaultdict
#use for loop to iterate over the lists
#start storing and attaching key value pair
#start increasing value for each key by 1
#iterate over the hashmap 
#anykey that has a value hogher than one we return True

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        hash_value = defaultdict(int)
        for i in nums:
            hash_value[i]+=1
        for key,value in hash_value.items():
            if value >1:
                return True
        return False            
        