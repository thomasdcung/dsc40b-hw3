def swap_sum(A, B):
    """Swaps two elements in two sorted arrays to obtain a target sum 
    difference of 10.

    Assumes that both arrays are sorted in ascending order and only 
    contain integers.

    """
    # TODO: Implement the swap_sum function
    sum_a = sum(A)
    sum_b = sum(B)

    diff = 10 - (sum_b - sum_a)
    if diff % 2 != 0:
        return None
    target = diff // 2 

    i, j = 0, 0
    while i < len(A) and j < len(B):
        b_needed = A[i] - target
        if B[j] == b_needed:
            return (i, j)
        elif B[j] < b_needed:
            j += 1
        else:
            i += 1

    return None
    