class Solution {
    public int[][] constructProductMatrix(int[][] g) {
        int n = g.length, m = g[0].length;
        int mod = 12345;
        int[] a = new int[n*m];
        int k = 0;        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                a[k++] = g[i][j] % mod;
            }
        }       
        int[] pre = new int[n*m];
        int[] suf = new int[n*m];
        
        pre[0] = 1;
        for(int i=1;i<n*m;i++){
            pre[i] = (pre[i-1] * a[i-1]) % mod;
        }
        
        suf[n*m-1] = 1;
        for(int i=n*m-2;i>=0;i--){
            suf[i] = (suf[i+1] * a[i+1]) % mod;
        }
        int[][] ans = new int[n][m];
        k = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                ans[i][j] = (pre[k] * suf[k]) % mod;
                k++;
            }
        }       
        return ans;
    }
}
