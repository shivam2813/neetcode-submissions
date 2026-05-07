class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data={}

        for n in nums:
            if n in data:
                print(n)
                return True
            data[n]=1
        return False