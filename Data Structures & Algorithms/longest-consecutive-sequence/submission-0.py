class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorteddata=sorted(set(nums))
        longeststreak=1
        current=1
        for i in range(1,len(sorteddata)):
            if sorteddata[i]==sorteddata[i-1]+1:
                current+=1
            else:
                longeststreak=max(longeststreak,current)
                current=1
        return max(longeststreak,current)

