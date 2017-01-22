---
layout: post
title: Solutions to Leetcode Contest 16
---

I feel Leetcode contest is a very good way to keep my coding skill on the right track. There are primarily two reasons.  

1. The contest is fun, and you can see others` better solutions and improve your coding skill.
2. The time is limited such that you can focus on the coding questions in such a time frame. 

There are two different sessions for contest 16: A & B. In total, there are 6 questions. Let me explain these questions one by one followed by my own solution.

### 484. Find Permutation
Initially I think the question is complex and simply use tree search to go through all possible permutations as the below code:
    
    /**
     * Created by wihoho on 21/1/17.
     */
    public class FindPermutation {
    
        public static void main(String[] args) {
            FindPermutation findPermutation = new FindPermutation();
            findPermutation.findPermutation("DI");
        }
    
        public int[] findPermutation(String s) {
            if (s == null || s.length() == 0) {
                return new int[0];
            }
    
            List<List<Integer>> result = new ArrayList<>();
            boolean[] taken = new boolean[s.length() + 2];
    
            for (int i = 1; i <= s.length() + 1; i++) {
                List<Integer> cur = new ArrayList<>();
                cur.add(i);
                taken[i] = true;
                helper(s, 0, taken, cur, result);
                taken[i] = false;
            }
    
            int[] ret = new int[result.get(0).size()];
            for(int i = 0; i < result.get(0).size(); i ++) {
                ret[i] = result.get(0).get(i);
            }
            return ret;
        }
    
        private void helper(String s, int currentIndex, boolean[] taken, List<Integer> cur, List<List<Integer>> result) {
            if (currentIndex == s.length()) {
                if (result.isEmpty()) {
                    result.add(new ArrayList<>(cur));
                } else if (compare(cur, result.get(0))) {
                    result.clear();
                    result.add(new ArrayList<>(cur));
                }
    
                return;
            }
    
            if (cur.isEmpty()) {
                return;
            }
    
            int last = cur.get(cur.size() - 1);
            char ch = s.charAt(currentIndex);
            if (ch == `D`) {
    
                for (int i = 1; i < last; i++) {
                    if (!taken[i]) {
                        cur.add(i);
                        taken[i] = true;
                        helper(s, currentIndex + 1, taken, cur, result);
                        taken[i] = false;
                        cur.remove(cur.size() - 1);
                    }
                }
    
            } else if (ch == `I`) {
    
                for (int i = last + 1; i < taken.length; i++) {
                    if (!taken[i]) {
                        cur.add(i);
                        taken[i] = true;
                        helper(s, currentIndex + 1, taken, cur, result);
                        taken[i] = false;
                        cur.remove(cur.size() - 1);
                    }
                }
    
            }
    
    
        }
    
        private boolean compare(List<Integer> l1, List<Integer> l2) {
            for (int i = 0; i < l1.size(); i++) {
                if (l1.get(i) < l2.get(i)) {
                    return true;
                } else if (l1.get(i) > l2.get(i)) {
                    return false;
                }
            }
    
            return false;
        }
    }


It turns out to be a rather bad idea because it takes longer time to search all possibilities. Later I find that that there is a better solution by performing manipulations on the array itself.

1. Firstly assumes that the input string comprises only "I". The array shall be increasing like 1,2,3,4,5...
2. Go through the input string, if the current character is "I", simply continue
3. If the character is "D", we have to swap the current item with the next item in the array such that the array is decreasing at this moment.
4. Moreover, we need to go back to check whether the previous char is also "D". If so, we have to swap again.
5. Repeat step 4 until there is no more "D" again.

The abobe steps could be explained the below code easily.

    /**
     * Created by wihoho on 22/1/17.
     */
    public class FindPermutationTwo {
        public int[] findPermutation(String s) {
            int size = s.length();
            int[] permutations = new int[size + 1];
            for (int i = 0; i <= size; i++) {
                permutations[i] = i + 1;
            }
    
            for (int i = 0; i < size; i++) {
                if (s.charAt(i) == `D`) {
                    int j = i;
    
                    while (j >= 0 && s.charAt(j) == `D`) {
                        swap(permutations, j, j + 1);
                        j--;
                    }
                }
            }
    
            return permutations;
        }
    
        private void swap(int[] arr, int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

### 494. Target Sum
This one is relatively easy. Like the initial thinking of the above question, we only need to perform tree search on this question to get the result. We can imagine that for each item there are only two cases: + or -. As a result, we can build a tree as below 

         1
        / \
      -1  +1
      
During the proecess, we just check whether the sum equals to the target or not,

    /**
     * Created by wihoho on 22/1/17.
     */
    public class TargetSum {
    
        public static void main(String[] args) {
            TargetSum targetSum = new TargetSum();
            int[] nums = {1,1,1,1,1};
            System.out.println(targetSum.findTargetSumWays(nums, 3));
        }
    
        public int findTargetSumWays(int[] nums, int S) {
            int[] ret = new int[1];
            helper(nums, 0,  S, 0, ret);
            return ret[0];
        }
    
        private void helper(int[] nums, int index, int S, int current, int[] ret) {
            if (index == nums.length) {
                if (current == S) {
                    ret[0] += 1;
                }
    
                return;
            }
    
            int temp = nums[index];
            helper(nums, index + 1, S, current + temp, ret);
            helper(nums, index + 1, S, current - temp, ret);
    
        }
    }

### 491. Increasing Subsequences
Just use the tree search, and perform duplicate check. There shall be better ways to filter the duplicate case like to avoid the duplicate recursion. But using the hashset to filter also works. 

    import java.util.ArrayList;
    import java.util.HashSet;
    import java.util.List;
    import java.util.Set;
    import java.util.stream.Collectors;
    
    /**
     * Created by wihoho on 22/1/17.
     */
    public class IncreasingSubsequences {
        public static void main(String[] args) {
            IncreasingSubsequences increasingSubsequences = new IncreasingSubsequences();
            int[] nums = {4,6,7,7};
            increasingSubsequences.findSubsequences(nums);
        }
    
        public List<List<Integer>> findSubsequences(int[] nums) {
            Set<List<Integer>> result = new HashSet<>();
    
            for(int i = 0; i < nums.length; i ++) {
                helper(nums, i, new ArrayList<>(), result);
            }
    
            return result.stream().collect(Collectors.toList());
        }
    
        private void helper(int[] nums, int index, List<Integer> cur, Set<List<Integer>> result) {
            if (index == nums.length) {
                return;
            }
    
            int temp = nums[index];
            if (cur.isEmpty()) {
                cur.add(temp);
            } else {
                if (temp >= cur.get(cur.size() - 1)) {
                    cur.add(temp);
                    result.add(new ArrayList<>(cur));
                    helper(nums, index + 1, cur, result);
                    cur.remove(cur.size() - 1);
                }
            }
    
            helper(nums, index + 1, cur, result);
        }
    }


### 492. Construct the Rectangle
As the requirements suggest that the difference between width and height shall be minimized, we can start from the middles point to see, which is `Math.sqrt(num)`. The next step is simply a while loop to check whether the area could be perfectly divisable by the width. If no, we continue to check by decreasing the width by 1.

    /**
     * Created by wihoho on 22/1/17.
     */
    public class ConstructRectangle {
        public static void main(String[] args) {
            ConstructRectangle constructRectangle = new ConstructRectangle();
            constructRectangle.constructRectangle(2);
        }
    
        public int[] constructRectangle(int area) {
            int width = (int) Math.sqrt(area);
    
            while (width >= 1) {
    
                if (area % width == 0) {
                    int height = area / width;
    
                    int[] ret = new int[2];
                    ret[0] = width;
                    ret[1] = height;
    
                    return ret;
                }
    
                width -= 1;
            }
    
            return new int[0];
        }
    }

### 486. Predict the Winner
This is a kind of game theory problem using dynamic programming to resolve. Firstly, we need to define a state which works for both players. To do so, 

* Define `dp[i][j]` to represent the max amount for the current player when numbers from position `i` to `j` are remained. 
* As a result, `dp[0][size-1]` is going to be the max amount to player 1.
* If `dp[0][size-1]` is larger than half of the total sum, namely `sum(a[0], a[1],...a[size-1])`, player 1 wins.

Now let's construct the transform function. There are two possibilities: take the left one or the right one. 
    
    dp[i][j] = sum[i][j] - min(dp[i+1][j], dp[i][j-1])
    
With the above info, the code becomes easy,

    /**
     * Created by wihoho on 22/1/17.
     */
    public class PredictWinner {
        public static void main(String[] args) {
    
            int[] nums = {1, 5, 2};
            PredictWinner predictWinner = new PredictWinner();
            System.out.println(predictWinner.PredictTheWinner(nums));
    
        }
    
        public boolean PredictTheWinner(int[] nums) {
            int size = nums.length;
    
            int[][] dp = new int[size][size];
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    dp[i][j] = -1;
                }
            }
    
            for (int i = 0; i < size; i++) {
                dp[i][i] = nums[i];
            }
    
            int[] sum = new int[size + 1];
            sum[1] = nums[0];
    
            for (int i = 2; i <= size; i++) {
                sum[i] = sum[i - 1] + nums[i - 1];
            }
    
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    if (i < j) {
    
                        dp[i][j] = helper(dp, i, j, nums, sum);
                    }
                }
            }
    
            int result = dp[0][size - 1];
            int total = sum[size];
    
            return result > total - result ? true : false;
        }
    
        private int helper(int[][] dp, int i, int j, int[] nums, int[] sum) {
            if (dp[i][j] != -1) {
                return dp[i][j];
            } else if (i == j) {
                dp[i][j] = nums[i];
                return dp[i][j];
            } else if (i < j) {
                int minVal = Math.min(helper(dp, i + 1, j, nums, sum), helper(dp, i, j - 1, nums, sum));
    
                dp[i][j] = sum[j + 1] - sum[i] - minVal;
                return dp[i][j];
            }
    
            return Integer.MAX_VALUE;
        }
    }


### 483. Smallest Good Base
Now it comes to the last question, I feel this one interesting is mainly because we can infer the solution from the requirements. Basically, we need to get an `x` which meets the below two criterias

1. n = x^m + x^(m-1) + ... + x + 1
2. `x` shall be minimized

As the note suggests, `The range of n is [3, 10^18].`. We can try brute force for `x` ranging from 2 to 2^20. This is going to cover all cases for m larger than 3. The reason is because `2^60 + 2 ^ 40 + 2^20 + 1 > 10^18`. The left cases are then for `m = 1 or 2`.

    /**
     * Created by wihoho on 22/1/17.
     */
    public class SmallestGoodBase {
        public static void main(String[] args) {
            SmallestGoodBase smallestGoodBase = new SmallestGoodBase();
            System.out.println(smallestGoodBase.smallestGoodBase("470988884881403701"));
        }
    
        public String smallestGoodBase(String n) {
            long number = Long.parseLong(n);
    
            long ret = 0;
            for (int i = 2; i < 1 << 20; i++) {
                if (check(number, i)) {
                    ret = i;
                    return String.valueOf(ret);
                }
            }
    
            long sqrt = (long) Math.sqrt(number);
            if (sqrt * sqrt + sqrt + 1 == number) {
                return String.valueOf(sqrt);
            }
    
            return String.valueOf(number - 1);
        }
    
        private boolean check(long n, long ret) {
            while (n != 0) {
                if (n % ret == 1) {
                    n /= ret;
                } else {
                    return false;
                }
            }
    
            return true;
        }
    }

