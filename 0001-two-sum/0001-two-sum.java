class Solution {
    public int[] twoSum(int[] nums, int target) {
        int diff = 0;
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i = 0;i<nums.length;i++){
            diff = target - nums[i];
            if(map.containsKey(diff)){
                return new int[]{map.get(diff),i}; 
            }
            map.put(nums[i],i);
        }
        return new int[]{};
    }
}