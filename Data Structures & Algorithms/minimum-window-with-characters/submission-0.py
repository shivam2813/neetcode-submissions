class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need={}
        for c in t:
            need[c]=need.get(c,0)+1

        have={}
        required=len(need)
        formed=0
        left=0
        best=""

        for right in range(len(s)):
            char=s[right]
            have[char]=have.get(char,0)+1

            if char in need and have[char]==need[char]:
                formed+=1
            
            while formed == required:
                window = s[left:right+1]

                if not best or len(window)<len(best):
                    best= window

                left_char=s[left]
                have[left_char]-=1
                if left_char in need and have[left_char]<need[left_char]:
                    formed-=1
                left +=1
        return best