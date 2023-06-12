#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dp[1000001];
vector<bool> status(1000001);
vector<int> island(1000001, -1);

int c = -1;
void cycle(int node)
{
    if(node == c)
        return;
    dp[node] = dp[c];
    cycle(island[node]);
}

int dfs(int node)
{
    if(dp[node] != 0)
        return dp[node];
    
    int cur = 0;
    if(island[node] != -1 && !status[island[node]])
    {
        status[island[node]] = 1;
        cur = dfs(island[node]);
    }
    else if(island[node] != -1 && dp[island[node]] == 0)
        c = island[node];
    else if(island[node] != -1)
        cur = dfs(island[node]);
    
    dp[node] = cur + 1;
    if(node == c)
    {
        cycle(island[c]);
        c = -1;
    }

    return dp[node];
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int m, n;
    cin >> m >> n;

    while(m--)
    {
        int u, v;
        cin >> u >> v;

        island[u] = v;
    }

    int result = 0;
    for(int i = 0; i < n; i++)
    {
        if(!status[i])
            status[i] = 1;
        result = max(result, dfs(i));
    }
        
    cout << result << "\n";
}