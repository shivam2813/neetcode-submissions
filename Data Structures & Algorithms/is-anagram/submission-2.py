class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t)!= len(s):
            return False

        temp= {}
        for char in s:
            temp[char]= temp.get(char,0)+1
        for char in t:
            if char not in temp or temp[char]==0:
                return False;
            temp[char]-=1
        return True


        