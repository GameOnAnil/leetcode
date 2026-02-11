class Solution {
  int findMaxConsecutiveOnes(List<int> nums) {
    int ans = 0;
    int count = 0;
    for(int i = 0; i < nums.length; i++){
        if(nums[i] == 1){
            count+=1;
        }
        else{
            ans = max(ans,count);
            count = 0;
        }
    }
    ans = max(ans,count);

    return ans;
  }
}