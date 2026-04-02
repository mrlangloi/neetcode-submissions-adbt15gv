class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        // initialize the frequency array with all array lists
        // the index of freq represents the frequency of each number
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        // count how many times each number appears in a hashmap
        // the key is the number, the value is the frequency
        for (int num : nums) {
            if (!count.containsKey(num)) {
                count.put(num, 1);
            } else {
                count.replace(num, count.get(num) + 1);
            }
        }

        // iterate through the hashmap
        // using the value as the freq index, add the key to the list in that index
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            // System.out.println("Key: " + entry.getKey() + "\tValue: " + entry.getValue());
            freq[entry.getValue()].add(entry.getKey());
        }

        // initialize result array
        // iterate through the freq array backwards
        // if we encounter any populated list, we add the numbers in the list
        // up until we hit k numbers in the res array, then we return res
        int[] res = new int[k];
        int resIndex = 0;
        for (int i = freq.length - 1; i > 0 && resIndex < k; i--) {
            for (int num : freq[i]) {
                res[resIndex] = num;
                resIndex++;
                if (resIndex == k) {
                    return res;
                }
            }
        }

        return res;
    }
}
