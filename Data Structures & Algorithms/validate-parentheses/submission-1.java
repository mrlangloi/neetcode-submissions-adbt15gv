class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> pMap = new HashMap<>();
        pMap.put(')', '(');
        pMap.put('}', '{');
        pMap.put(']', '[');

        char[] sArr = s.toCharArray();

        for (char c : sArr) {
            if (pMap.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == pMap.get(c)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}
