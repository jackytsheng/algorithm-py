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
            j -= 1
    # Algorithm ends
    toc = time.perf_counter()
    print_detail and print_detail_helper(len(nums), toc-tic)


def merge_sort(nums: list[int | float], print_detail: False):
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
    pass


def print_detail_helper(element_length, time_diff):
    print("Elements Length in array {}".format(element_length))
    print("Execution takes {0:.4f} seconds".format(time_diff))
