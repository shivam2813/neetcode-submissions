class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>mpp;
        for(int i=0;i<nums.size();i++)
        {
            int subtracted= target-nums[i];
            if(mpp.find(subtracted)!=mpp.end())
            {
                return {mpp[subtracted],i};
            }
            mpp[nums[i]]=i;
        }
        return {};
    }
};
