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


my_list = [4, 6, 1, 7, 3, 2, 5]
print(pivot(my_list, 0, len(my_list) - 1))
