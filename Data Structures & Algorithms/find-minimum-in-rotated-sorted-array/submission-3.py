class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum=1001
        start=0
        end=len(nums)-1

        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]<minimum:
                minimum=nums[mid]

            if nums[mid]<nums[end]:
                end=mid-1
            else:
                start=mid+1
        return minimum

