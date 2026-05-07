class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s)!=len(t):
        return False
      mpp={}
      for char in s:
        if char in mpp:
            mpp[char]+=1
        else:
            mpp[char]=1
    
      for char in t:
        if char not in mpp or mpp[char]==0:
            return False
        else:
            mpp[char]-=1
      return True