class Solution {
  int findNumbers(List<int> nums) {
    int totalEven =0;
    for(int i in nums)
    {
       final len= i.toString().split('').length;
        if(len%2==0) totalEven++;
    }
      return totalEven;
  }
}