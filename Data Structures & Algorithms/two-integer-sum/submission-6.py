class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      data={}
      for i,num in enumerate(nums):
        complement=target-num
        if complement in data:
            return [data[complement],i]
        data[num]=i
      return []