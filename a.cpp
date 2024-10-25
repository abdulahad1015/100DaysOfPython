#include <bits/stdc++.h>

#define forn(a, b) for(int i = a; i < b; ++i)
#define form2n(i, a, b) for(int i = a; i < b; ++i)
#define int unsigned long long int
#define nl cout << "\n"
#define debug(x) cout << #x << ": " << x << ", "
#define vi vector<int>
#define pb(x) push_back(x)
#define all(x) x.begin(), x.end()
#define hhh cout << "here" << "\n"

using namespace std;

void solve(){
    int n,k,count=1;
    cin>>n>>k;
    bool flag=true;
    string s;
    cin>>s;
    while(flag){
        count=0;
        flag = false;

        forn(1,s.length()-1){
            if(s[i]==s[i-1])
                count++;
            if(count==k-1){
                s.erase(i-(k-2),k);
                flag=true;2
                break;
            }      
        }
    }
    cout<<s<<endl;
    
}

signed main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t = 1;
    // cin >> t;
    // forn(0, t){
        solve();
        // cout<<endl;
    // }

    return 0;
}