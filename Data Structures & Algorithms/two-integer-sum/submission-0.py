class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        result = []

        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]]= i
            else:
                if i < dict.get(target - nums[i]):
                    result[0] = i
                    result[1] = dict.get(target - nums[i])
                   
                else:
                    return [dict.get(target - nums[i]), i]

        return result





        