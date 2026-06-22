class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        m = len(nums)
        while i<= m and j <= m:
            j+=1
            if i !=j:
                if nums[i] + nums[j] == target:
                    return [i,j]
            if j== len(nums)-1:
                i+=1
                j=0

