def swap(_my_list, idx1, idx2):
    _my_list[idx1], _my_list[idx2] = _my_list[idx2], _my_list[idx1]


def pivot(_my_list, pivot_idx, end_idx):
    swap_idx = pivot_idx

    for i in range(pivot_idx + 1, end_idx + 1):
        if _my_list[i] < _my_list[pivot_idx]:
            swap_idx += 1
            swap(_my_list, swap_idx, i)
    swap(_my_list, pivot_idx, swap_idx)
    return swap_idx


def quick_sort_helper(_my_list, left, right):
    if left < right:
        pivot_idx = pivot(_my_list, left, right)
        quick_sort_helper(_my_list, left, pivot_idx - 1)
        quick_sort_helper(_my_list, pivot_idx + 1, right)
    return _my_list


def quick_sort(_my_list):
    return quick_sort_helper(_my_list, 0, len(_my_list) - 1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
