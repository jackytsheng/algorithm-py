import random
import pytest
from sorting import bubble_sort, insert_sort, merge_sort, quick_sort

random_list = [random.randint(1, 1000) for _ in range(1000)]


@pytest.mark.parametrize('lst, expected', [
    ([], []),
    ([1], [1]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, 2, 4, 2, 1, 4, 3], [1, 2, 2, 3, 3, 4, 4]),
    ([-5, 3, -2, 10, 0, -1], [-5, -2, -1, 0, 3, 10]),
    ([3.14, 2.5, 1.618, 4.2, 0.1], [0.1, 1.618, 2.5, 3.14, 4.2]),
    ([2, 1, 3, 2, 1, 3, 2, 1, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    (random_list, sorted(random_list))
])
def test_bubble_sort(lst, expected):
    bubble_sort(lst)
    assert lst == expected


@pytest.mark.parametrize('lst, expected', [
    ([], []),
    ([1], [1]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, 2, 4, 2, 1, 4, 3], [1, 2, 2, 3, 3, 4, 4]),
    ([-5, 3, -2, 10, 0, -1], [-5, -2, -1, 0, 3, 10]),
    ([3.14, 2.5, 1.618, 4.2, 0.1], [0.1, 1.618, 2.5, 3.14, 4.2]),
    ([2, 1, 3, 2, 1, 3, 2, 1, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    (random_list, sorted(random_list))
])
def test_insert_sort(lst, expected):
    insert_sort(lst)
    assert lst == expected


@pytest.mark.parametrize('lst, expected', [
    ([], []),
    ([1], [1]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, 2, 4, 2, 1, 4, 3], [1, 2, 2, 3, 3, 4, 4]),
    ([-5, 3, -2, 10, 0, -1], [-5, -2, -1, 0, 3, 10]),
    ([3.14, 2.5, 1.618, 4.2, 0.1], [0.1, 1.618, 2.5, 3.14, 4.2]),
    ([2, 1, 3, 2, 1, 3, 2, 1, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    (random_list, sorted(random_list))
])
def test_quick_sort(lst, expected):
    quick_sort(lst)
    assert lst == expected


@pytest.mark.parametrize('lst, expected', [
    ([], []),
    ([1], [1]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, 2, 4, 2, 1, 4, 3], [1, 2, 2, 3, 3, 4, 4]),
    ([-5, 3, -2, 10, 0, -1], [-5, -2, -1, 0, 3, 10]),
    ([3.14, 2.5, 1.618, 4.2, 0.1], [0.1, 1.618, 2.5, 3.14, 4.2]),
    ([2, 1, 3, 2, 1, 3, 2, 1, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    (random_list, sorted(random_list))
])
def test_merge_sort(lst, expected):
    merge_sort(lst)
    assert lst == expected
