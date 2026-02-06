class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();   // FIX 1

        int count = 0;
        int n = s.length();

        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') {  // FIX 2
                break;
            } else {
                count++;
            }
        }
        return count;
    }
}
