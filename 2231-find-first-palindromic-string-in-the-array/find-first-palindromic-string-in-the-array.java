class Solution {
    public String firstPalindrome(String[] words) {
        for(int i = 0; i < words.length; i++){
            String reversed = new StringBuilder(words[i]).reverse().toString();
            if (words[i].equals(reversed)){ return words[i];}
        }
        return "";
    }
}
