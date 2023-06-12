
class Solution {
  int findMaxConsecutiveOnes(List<int> nums) {
    int count = 0;
    int max = 0;
    for (int i = 0; i <= nums.length - 1; i++) {
      if (nums[i] == 1) {
        count++;
      } else {
        count = 0;
      }
      if (max < count) {
        max = count;
      }
      print("max" + max.toString());
      print("count" + count.toString());
    }
    return max;
  }
}
