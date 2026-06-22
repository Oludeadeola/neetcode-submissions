class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i=0
        n = len(nums)
        ans = []
        m=0
        while m<2*n:
            if i == n:
                i=0
            ans+=[nums[i]]
            i+=1
            m+=1

        return ans    
