class Solution {
public:
    int smallestNumber(int n, int t) {
        for(int i = n; i < n+10; ++i) {
            int p = 1;
            int ans = i;
            int i2 = i;
            while(i2) {
                p *= (i2%10);
                i2 /= 10;
            }
            if(p%t == 0)
                return ans;
        }
        return 0;
    }
};
