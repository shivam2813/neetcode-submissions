class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>res;
        for(auto s:strs)
        {
            string sortedres=s;
            sort(sortedres.begin(),sortedres.end());
            res[sortedres].push_back(s);
        }
        vector<vector<string>>result;
        for(auto pair:res)
        {
            result.push_back(pair.second);
        }
        return result;
         
    }
};
