class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int n = grid.size();
        int m = grid[0].size();
        k = k % (n*m);
        vector<vector<int>> ans(n, vector<int>(m, 0));
        int t = m*n;

        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                int c = i*m+j;
                int r = (c+k) % t;
                
                int ni = r/m;
                int nj = r%m;

                ans[ni][nj] = grid[i][j];
            }
        }
        return ans;
    }
};
