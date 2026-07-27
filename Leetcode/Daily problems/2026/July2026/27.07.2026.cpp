class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int a = nums[0], b = nums[1];
        if(a < b) {
            int c = a;
            a = b;
            b = c;
        }
        for(int i=2; i<nums.size(); i++) {
            // cout << a << b;
            if(nums[i]>=a) {
                b = a;
                a = nums[i];
            }
            else if(nums[i]>b)
                b = nums[i];
        }
        return (a-1)*(b-1);
    }
};
