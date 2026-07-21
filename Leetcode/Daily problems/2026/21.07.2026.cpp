class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        int n = s.size();
        int one = count(s.begin(), s.end(), '1');
        if(one==0)
            return 0;

        int i = 0;
        int prev = INT_MIN, curr = 0, z = 0;

        while(i < n) {
            int st = i;

            while(i<n && s[i]==s[st])
                i++;

            if(s[st] == '0') {
                curr = i-st;
                z = max(z, prev+curr);
                prev = curr;
            }
        }
        return one + z;
    }
};
