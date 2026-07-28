class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int> cnt(123, 0);
        for(char c:s)
            cnt[c]++;
        
        int n=s.size();
        int l=0, r=n-1, m=n/2;
        for(char ch='a'; ch<='z'; ch++){
            int c=cnt[ch];

            while(c>1){
                s[l++] = s[r--] = ch;
                c -= 2;
            }
            if(c) s[m] = ch;
        }
        return s;
    }
};
