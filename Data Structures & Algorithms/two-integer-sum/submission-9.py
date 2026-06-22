class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data={}

        for i in range(len(nums)):
            Rem=target-nums[i]
            if Rem in data:
                return [data[Rem],i]
            data[nums[i]]=i
        return []

