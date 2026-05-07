class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mpp={}
        for num in nums:
            if num in mpp:
                return True
            mpp[num]=True
        return False