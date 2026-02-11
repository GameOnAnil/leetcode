class Solution {
  List<int> getConcatenation(List<int> nums) {
    int n = nums.length;

    if(n == 0){
        return [];
    }
    List<int> ans = List.filled(2 * n, 0);
    for(int i=0; i < n;i++){
        ans[i] = nums[i];
        ans[i+n] = nums[i];
    }
    return ans;
  }
}