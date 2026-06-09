class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        data={}

        for c in s:
            if c not in data:
                data[c]=1
            else:
                data[c]+=1
        
        for c in t:
            if c in data:
                if data[c]== 0:
                    return False
                data[c]-=1
            else:
                return False

        return True