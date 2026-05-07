class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total=0
        for num in digits:
            total*=10
            total+=num
        total=total+1
        result=[]
        while total>0:
            digit=total%10
            total=total//10
            result.append(digit)
        result.reverse()
        return result
            