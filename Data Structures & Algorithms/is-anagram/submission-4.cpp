class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size())
        {
            return false;
        }
        unordered_map<char,int>data;
        for(char ch:s)
        {
            data[ch]+=1;
        }
        for(char ch:t)
        {
            if(data.find(ch)==data.end() || data[ch]==0)
            {
                return false;
            }
            data[ch]-=1;
        }
        return true;

    }
};
