class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        data={}
        for i in range(0,len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                currentSum=nums[i]+nums[j]+nums[k]
                if currentSum==0:
                    triplet=sorted([nums[i],nums[j],nums[k]])
                    if tuple(triplet) not in data:
                        data[tuple(triplet)]=1
                        result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif currentSum<0:
                    j+=1
                else:
                    k-=1
                    
        return result
                        

                            
                