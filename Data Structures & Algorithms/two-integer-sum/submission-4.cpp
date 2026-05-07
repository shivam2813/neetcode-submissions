class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> data;
        for(int i=0;i<nums.size();i++)
        {
            int compliment=target-nums[i];
            if(data.find(compliment)!=data.end())
            {
                return {data[compliment],i};
            }
            data[nums[i]]=i;
        }
        return {};
    }
};
