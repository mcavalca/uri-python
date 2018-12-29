def maxDistance(array):

    # max and min variables as described
    # in algorithm.
    max1 = -2147483648
    min1 = +2147483647
    max2 = -2147483648
    min2 = +2147483647

    for i in range(len(array)):


        # Updating max and min variables
        # as described in algorithm.
        max1 = max(max1, array[i] + i)
        min1 = min(min1, array[i] + i)
        max2 = max(max2, array[i] - i)
        min2 = min(min2, array[i] - i)


    # Calculating maximum absolute difference.
    return max(max1 - min1, max2 - min2)


# Driver program to
# test above function

array = [ 17, 55, 3, 53, 23, 19, 27, 76, 93, 53, 42, 3, 32, 45, 95, 0, 48, 90, 20, 68, 7, 9, 67, 57, 4, 45, 66, 70, 28, 61, 56, 22, 25, 52, 89, 17, 89, 19, 49, 65, 40, 90, 54, 25, 34, 70,
51 ]

print(maxDistance(array))
