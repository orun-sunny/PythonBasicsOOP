def CountingEvenOdd(arr, arr_size):
    even_count = 0
    odd_count = 0

    # loop to read all the values
    # in the array
    for i in range(arr_size):

        # checking if a number is
        # completely divisible by 2
        if (arr[i] & 1 == 1):
            odd_count += 1
        else:
            even_count += 1

    print("Number of even elements = ",
          even_count)
    print("Number of odd elements = ",
          odd_count)


# Driver Code
arr = [2, 3, 4, 5, 6]
n = len(arr)

# Function Call
CountingEvenOdd(arr, n)
