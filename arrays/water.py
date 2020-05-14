def maxWater(arr, n) :

    # To store the maximum water
    # that can be stored
    res = 0;

    # For every element of the array
    for i in range(1, n - 1) :

        # Find the maximum element on its left
        left = arr[i];
        for j in range(i) :
            left = max(left, arr[j]);

            # Find the maximum element on its right
        right = arr[i];

        for j in range(i + 1 , n) :
            right = max(right, arr[j]);

            # Update the maximum water
        res = res + (min(left, right) - arr[i]);

    return res;

def findWater(arr, n):

    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0]*n

    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n

    # Initialize result
    water = 0

    # Fill left array
    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])

        # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);

        # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water

# Python program to find
# maximum amount of water that can
# be trapped within given set of bars.
# Space Complexity : O(1)

def findWater_2(arr, n):

    # initialize output
    result = 0

    # maximum element on left and right
    left_max = 0
    right_max = 0

    # indices to traverse the array
    lo = 0
    hi = n-1

    while(lo <= hi):

        if(arr[lo] < arr[hi]):

            if(arr[lo] > left_max):

                # update max in left
                left_max = arr[lo]
            else:

                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo+= 1

        else:

            if(arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi-= 1

    return result


# This code is contributed
# by Anant Agarwal.

# Driver code
if __name__ == "__main__" :

    arr = [4, 1, 1, 2, 1, 1, 3, 1, 1, 1, 1]
    #arr = [2, 1, 3, 1, 1, 0, 3]
    n = len(arr);

    print(findWater_2(arr, n));