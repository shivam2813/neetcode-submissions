class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        data={}
        for char in s:
            if char not in data:
                data[char]=1
            else:
                data[char]+=1
        
        for char in t:
            if char in data:
                if data[char]==0:
                    return False
                data[char]-=1
            else:
                return False
        
        return True