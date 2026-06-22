class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0
        j =0
        m = len(nums)
        ans = []
        while j <2*m:
            if i == m :
                i = 0
            ans += [nums[i]]
            i+=1
            j+=1
        return ans           