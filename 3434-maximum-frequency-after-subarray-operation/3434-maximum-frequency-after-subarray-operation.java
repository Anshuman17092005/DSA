class Solution {
    public int maxFrequency(int[] nums, int k) {
        int n = nums.length;
        int base = 0;
        for(int i = 0;i<n;i++){
            if(nums[i] == k) base++;
        }

        HashSet<Integer> set = new HashSet<>();
        for(int i = 0;i<n;i++){
            if(nums[i] != k){
                set.add(nums[i]);
            }
        }

        List<Integer> unique = new ArrayList<>(set);
        int maxgain = 0;
        for(int idx = 0;idx < unique.size();idx++){
            int val = unique.get(idx);
            int curr = 0;
            int best = 0;
            for(int i = 0;i<n;i++){
                if(nums[i] == val){
                    curr++;
                }
                else if(nums[i] == k){
                    curr--;
                }

            if(curr < 0){
                curr = 0;
            }
            if(curr > best){
                best = curr;
            }
        }
        if(best > maxgain){
            maxgain = best;
        }
        }
        return base+maxgain;
    }
}