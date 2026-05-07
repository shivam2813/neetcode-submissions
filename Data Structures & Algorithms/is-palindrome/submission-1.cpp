class Solution {
public:
    bool isPalindrome(string s) {
        string st;
        for(char c:s)
        {
            if(iswalnum(c))
            {
                st+=tolower(c);
            }
        }
        int i=0;
        int j=st.size()-1;

        while(i<j)
        {
            if(st[i]!=st[j])
            {
                cout<<st[i]<<st[j];
                return false;
            }
            else{
                i++;
                j--;
            }
        }
        return true;
    }
};
