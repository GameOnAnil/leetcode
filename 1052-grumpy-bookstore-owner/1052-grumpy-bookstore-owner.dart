class Solution {
  int maxSatisfied(List<int> customers, List<int> grumpy, int minutes) {
    int currSum = 0;
    int n = customers.length;
    for(int i = 0;i < n;i++){
        if(grumpy[i] == 0){
            currSum+=customers[i];
        }
    }
    int res = 0;
    for(int r = 0;r<n;r++){
        if(grumpy[r]==1){
            currSum+=customers[r];
        }
        int l = r-minutes;
        if(l>=0 && grumpy[l]==1){
            currSum-=customers[l];
        }
        res = max(res,currSum);
    }
    return res; 
  }
}