import time


def bubble_sort(nums: list[int | float], print_detail: bool = False):
    """
    nums: Sort int array,
    print_detail: enable detail to be print

    Worst complexity: n^2
    Average complexity: n^2
    Best complexity: n
    Space complexity: 1
    Method: Exchanging
    Stable: Yes
    Class: Comparison sort
    Optimisation: Nth pass sort nth value, so don't need to run the full list at the end 
    """

    tic = time.perf_counter()
    # Algorithm begins
    n = len(nums)
    if n < 2:
        toc = time.perf_counter()
        print_detail and print_detail_helper(len(nums), toc-tic)
        return nums
    while True:
        swap = False
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                swap = True
                nums[i], nums[i+1] = nums[i+1], nums[i]
        n -= 1
        if not swap or n == 1:
            break
    # Algorithm ends
    toc = time.perf_counter()

    print_detail and print_detail_helper(len(nums), toc-tic)


def insert_sort(nums: list[int | float], print_detail: bool = False):
    """
    nums: Sort int array,
    print_detail: enable detail to be print

    Worst complexity: n^2
    Average complexity: n^2
    Best complexity: n
    Space complexity: 1
    Method: Insertion
    Stable: Yes
    """

    tic = time.perf_counter()
    # Algorithm begins
    if len(nums) < 2:
        toc = time.perf_counter()
        print_detail and print_detail_helper(len(nums), toc-tic)
        return nums

    for i in range(1, len(nums)):
        j = i
        while j > 0:
            if nums[j-1] > nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break
            j -= 1
    # Algorithm ends
    toc = time.perf_counter()
    print_detail and print_detail_helper(len(nums), toc-tic)


def merge() -> list[int | float]:
    pass


def merge_sort_helper(nums) -> list[int | float]:

    # check base case, [], [n] is sorted by default
    if len(nums) < 2:
        return

    # get the mid point
    mid = len(nums) // 2

    # break array into left and right
    left_array = nums[:mid]
    right_array = nums[mid:]

    # assume passing in helper will sort both array
    merge_sort_helper(left_array)
    merge_sort_helper(right_array)

    # merge back the two part
    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            nums[k] = left_array[i]
            i += 1
        else:
            nums[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        nums[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        nums[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(nums: list[int | float], print_detail: bool = False):
    """
    nums: Sort int array,
    print_detail: enable detail to be print

    Worst complexity: n*log(n)
    Average complexity: n*log(n)
    Best complexity: n*log(n)
    Space complexity: n
    Method: Merging
    Stable: Yes
    """

    tic = time.perf_counter()

    # Algorithm begins
    if len(nums) < 2:
        toc = time.perf_counter()
        print_detail and print_detail_helper(len(nums), toc-tic)
        return nums

    # assume nums passed in will be mutated and sorted
    merge_sort_helper(nums)

    # Algorithm ends
    toc = time.perf_counter()
    print_detail and print_detail_helper(len(nums), toc-tic)


def quick_sort_helper(nums: list[int | float]) -> list[int | float]:
    if len(nums) < 1:
        return nums
    # choose the last one as pivot
    pivot = nums[-1]
    l = None
    for i in range(len(nums)-1):
        if nums[i] > pivot and l == None:
            l = i
        elif nums[i] < pivot:
            if not l:
                l = i+1
            else:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1

    nums[l], nums[-1] = nums[-1], nums[l]
    return quick_sort_helper(nums[:l]) + [nums[l]] + quick_sort_helper(nums[l+1:])


# Quick sort in Python

# function to find the partition position
def quick_sort_partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1

            # swapping element at i with element at j
            array[i], array[j] = array[j], array[i]

    # swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # return the position from where partition is done
    return i + 1

# function to perform quicksort


def quick_sort_helper(array, low, high):
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = quick_sort_partition(array, low, high)

        # recursive call on the left of pivot
        quick_sort_helper(array, low, pi - 1)

        # recursive call on the right of pivot
        quick_sort_helper(array, pi + 1, high)


def quick_sort(nums: list[int | float], print_detail: bool = False) -> list[int | float]:
    """
    nums: Sort int array,
    print_detail: enable detail to be print

    Worst complexity: n^2
    Average complexity: n*log(n)
    Best complexity: n*log(n)
    Method: Partitioning
    Stable: No
    Class: Comparison sort
    """

    tic = time.perf_counter()
    # Algorithm begins
    if len(nums) < 2:
        toc = time.perf_counter()
        print_detail and print_detail_helper(len(nums), toc-tic)
        return nums
    result = quick_sort_helper(nums, 0, len(nums)-1)
    # Algorithm ends
    toc = time.perf_counter()
    print_detail and print_detail_helper(len(nums), toc-tic)
    return result


def print_detail_helper(element_length, time_diff):
    print("Elements Length in array {}".format(element_length))
    print("Execution takes {0:.4f} seconds".format(time_diff))
