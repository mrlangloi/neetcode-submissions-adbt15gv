class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            int[] count = new int[26];
            char[] sArr = s.toCharArray();
            for (char c : sArr) {
                count[c - 'a']++;
            }
            String countStr = Arrays.toString(count);
            if (!map.containsKey(countStr)) {
                map.put(countStr, new ArrayList<>());
            }
            map.get(countStr).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
