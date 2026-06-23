class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        data={}
        i=0
        data[s[i]]=1
        maxCharSize=1
        for j in range(len(s)):
            if s[j] in data:
                while s[j] in data and i<j:
                    del data[s[i]]
                    i+=1
            data[s[j]]=1
            maxCharSize=max(maxCharSize,j-i+1)
        return maxCharSize


            