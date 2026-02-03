class Solution {
    public int jump(int[] nums) {
        int jumps=0,l=0,r=0;
        while(r<nums.length-1){
            int far = 0;
            for(int ind = l;ind <= r;ind++){
                far = Math.max(ind+nums[ind],far);
            }
            l=r+1;
            r=far;
            jumps++;
        }
        return jumps;
    }
}