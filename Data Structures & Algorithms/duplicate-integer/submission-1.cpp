class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> repeat;
        for(int num:nums)
        {
            if(repeat.find(num)!=repeat.end())
            {
                return true;
            }
            repeat.insert(num);
        }
        return false;

    }
};
