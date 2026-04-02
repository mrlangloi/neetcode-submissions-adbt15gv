class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sCharCount = new HashMap<>();
        char[] sArr = s.toCharArray();
        for (char c : sArr) {
            if (!sCharCount.containsKey(c)) {
                sCharCount.put(c, 1);
            } else {
                sCharCount.replace(c, sCharCount.get(c) + 1);
            }
        }

        Map<Character, Integer> tCharCount = new HashMap<>();
        char[] tArr = t.toCharArray();
        for (char c : tArr) {
            if (!tCharCount.containsKey(c)) {
                tCharCount.put(c, 1);
            } else {
                tCharCount.replace(c, tCharCount.get(c) + 1);
            }
        }

        return sCharCount.equals(tCharCount);
    }
}
