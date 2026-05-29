class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n=heights.size();
        int maxAmount = 0;
        int i=0,j=n-1;
        while(i<j){
            int currentAmount=min(heights[i],heights[j])*(j-i);
            maxAmount=max(currentAmount,maxAmount);
            if(heights[i]<heights[j])
            {
                i++;
            }
            else{
                j--;
            }
        }
        return maxAmount;
        
    }
};
