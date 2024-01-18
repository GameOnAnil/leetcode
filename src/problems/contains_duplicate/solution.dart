class Solution {
  bool containsDuplicate(List<int> nums) {
    if (nums.length == 0) return false;
    nums.sort();
    for (var i = 1; i < nums.length; i++) {
      if (nums[i] == nums[i - 1]) return true;
    }
    return false;
  }
}
