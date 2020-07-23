#
# Your previous Java content is preserved below:
#
# import java.io.*;
# import java.util.*;
#
# /*
#  * To execute Java, please define "static void main" on a class
#  * named Solution.
#  *
#  * If you need more classes, simply define them inline.
#  */
#
# class Solution {
#   public static void main(String[] args) {
#     ArrayList<String> strings = new ArrayList<String>();
#     strings.add("Hello, World!");
#     strings.add("Welcome to CoderPad.");
#     strings.add("This pad is running Java " + Runtime.version().feature());
#
#     for (String string : strings) {
#       System.out.println(string);
#     }
#   }
#
#   // num % 2 == 0;  // even, otherwise odd.
#
#   private static int getOutlier(int[] arr) {
#
#
#
#     return 0;
#   }
#
# }
#
def get_outlier(arr):
    num_odds = 0
    num_even = 0
    is_first_odd = False
    if arr[0] % 2 == 1:
        num_odds += 1
        is_first_odd = True
    else:
        num_even += 1

    if arr[1] % 2 == 1:
        num_odds += 1
    else:
        num_even += 1

    if num_odds == 2:
        for item in arr[2:]:
            if item % 2 == 0:
                return item

    elif num_even == 2:
        for item in arr[2:]:
            if item % 2 == 1:
                return item

    elif num_odds == 1 and num_even == 1:
        if arr[2] % 2 == 1:
            if not is_first_odd:
                return arr[0]
            else:
                return arr[1]
        elif arr[2] % 2 == 0:
            if is_first_odd:
                return arr[0]
            else:
                return arr[1]

def find_outliner(a):
    if a[0] % 2 != a[1] % 2:
        return a[0] if a[2] % 2 == a[1] % 2 else a[1]
    for i in a:
        if i % 2 != a[0] % 2:
            return i

# [1, 2, 4, 6, 8, 10] => 1
# [2, 1, 4, 6, 8, 10] => 1
# [2, 4, 1, 6, 8, 10] => 1
# [2, 4, 6, 6, 8, 1] => 1

# [2, 3, 3, 5, 9, 7] => 2
# [3, 2, 3, 5, 9, 7] => 2
# [3, 3, 2, 5, 9, 7] => 2
# [1, 3, 3, 5, 9, 2] => 2


print(get_outlier([1, 3, 3, 5, 9, 2]))

