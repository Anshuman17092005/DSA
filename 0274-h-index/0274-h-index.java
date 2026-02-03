class Solution {
    public int hIndex(int[] citations) {
        // int h =0;
        // while(h <= citations.length){
        //     int cnt = 0;
        //     for(int i = 0;i<citations.length;i++){
        //         if(h<=citations[i]){
        //             cnt++;
        //         }
        //     }
        //     if(cnt >= h){
        //             h++;
        //         }else{
        //             break;
        //         }
        // }
        // return h-1;
        int n = citations.length;
        Arrays.sort(citations);
        for(int i = 0;i<citations.length;i++){
            if(citations[i] >= n - i){
                return n - i;
            }
        }
        return 0;
    }
}