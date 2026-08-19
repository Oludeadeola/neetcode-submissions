#using the hash method valled seen
#i will loop thriough the lists,i will start by picking one value one after the otehr..
#once a value is picked, i will substarct it from the target becuase the number must always be less than target
#i will check if that number is in target
#then i will return the number if it is and fasle if it is not
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         seen = {}
         count =0
         for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]]= count
            count+=1

