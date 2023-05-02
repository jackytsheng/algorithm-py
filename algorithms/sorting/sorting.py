
import time


def in_place_int_bubble_sort(nums: list[int | float], print_detail: False):
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


def print_detail_helper(element_length, time_diff):
    print("Elements Length in array {}".format(element_length))
    print("Execution takes {0:.4f} seconds".format(time_diff))
