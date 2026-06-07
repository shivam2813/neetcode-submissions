class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data={}

        for num in nums:
            if num not in data:
                data[num]=1
            else:
                return True

        return False