#include<bits/stdc++.h>
using namespace std;



//Given an array of integers and a ls,return true if any subset of the array's sum
//equals ls

//8 10 1 3 ls=12
//Choose:8
//Choose:10
//Choose:1
//Choose:3

//8,1,3
//Output:Yes

//5 5 5 ls=16
//Output:No

//Choose not choose

// At first index: choose number or dont choose

int dp[501][1001];

bool helper(vector<int>&a,int n,int index,int ls,int rs){

    if(rs==ls){
        return true;
    }
    if(index==n){
        return false;
    }
    if(dp[index][rs]!=-1){
        return (bool)dp[index][rs];
    }

    if(rs+a[index]>ls-a[index]){
        bool skip = helper(a,n,index+1,ls,rs);
        return dp[index][rs]=skip;
    }


    bool notChoose=helper(a,n,index+1,ls,rs);
    bool choose = helper(a,n,index+1,ls-a[index],rs+a[index]);
    return dp[index][rs]=(notChoose||choose)||(max(notChoose,choose));

}

bool isSubset(vector<int>&a,int n,int ls){
    return helper(a,n,0,ls,0);
}
int main(){

    memset(dp,-1,sizeof(dp));
    int n;
    cin>>n;
    vector<int>a(n);
    int sum=0;
    for(int i=0;i<n;++i){cin>>a[i];
    sum+=a[i];
    }
    cout<<isSubset(a,n,sum);
}


int max_match(string c, string s){

    int i = s.length()-1;
    int j=c.length()-1;
    int count=0,maxs,maxc;
    while(s[i]==c[j] && i>=0 && j>=0){
        count ++;
        i--;
        j--;
    }
    string temp; 
    if(i!=0){
        temp=s;
        s.pop_back();
        maxs=max_match(s,c);
        s=temp;
    }
    if(j!=0){
        temp=c;
        c.pop_back();
        maxc=max_match(s,c);
        c=temp;
    }
    return max(count,max(maxs,maxc));

}