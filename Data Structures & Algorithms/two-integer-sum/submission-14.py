class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in dict_num.keys():
                return [dict_num[value], i]
            dict_num[nums[i]] = i
