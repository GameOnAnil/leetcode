class Solution {
  List<int> twoSum(List<int> nums, int target) {
    Map<int,int> seen = Map<int,int>();
    for(int i= 0; i < nums.length; i++){
        final value = nums[i];
        if (seen.containsKey(target - value)){
            return [seen[target-value]!,i];
        }
        seen[value] = i;
    }
    return [];
  }
}