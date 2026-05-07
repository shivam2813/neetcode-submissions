class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>data;
        for(auto s:strs)
        {
            string sortedres=s;
            sort(sortedres.begin(),sortedres.end());
            data[sortedres].push_back(s);
        }
        vector<vector<string>>result;
        for(auto pair:data)
        {
            result.push_back(pair.second);
        }
        return result;

    }
};
