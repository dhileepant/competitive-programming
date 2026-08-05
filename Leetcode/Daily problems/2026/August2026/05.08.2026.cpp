class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> edges(n);
        for(auto i : invocations)
            edges[i[0]].push_back(i[1]);
        
        queue<int> q;
        q.push(k);
        vector<int> vis(n, 0);

        while(!q.empty()) {
            int nd = q.front();
            q.pop();

            vis[nd] = 1;

            for(int i : edges[nd])
                if(!vis[i])
                    q.push(i);
            
        }

        int f = 0;
        for(auto i : invocations) {
            if(vis[i[0]]==0 && vis[i[1]]){
                f = 1;
                break;
            }
        }

        vector<int> ans;
        for(int i = 0; i < n; ++i) {
            if(f)
                ans.push_back(i);
            else if(vis[i]==0)
                ans.push_back(i);
        }

        return ans;
    }
};
