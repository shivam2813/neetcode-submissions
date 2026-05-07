class Solution {
public:
    int lengthOfLongestSubstring(string s) {
      unordered_map<char,int>cmap;
      int l=0,res=0;
      for(int r=0;r<s.size();r++)
      {
        if(cmap.find(s[r])!=cmap.end())
        {
            l=max(cmap[s[r]]+1,l);
        }
        cmap[s[r]]=r;
        res=max(r-l+1,res);
      }
      return res;
      
    }
};
