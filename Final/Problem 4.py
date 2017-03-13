def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    start_i = 0
    end_i = 0
    inc_i = 0
    dec_i = 0

    for i in range(len(L) - 1):
        if L[i] <= L[i + 1]:
            dec_i += 1
            if dec_i > start_i:
                start_i = dec_i
                end_i = i + 1
        else:
            dec_i = 0
        if L[i] >= L[i + 1]:
            inc_i += 1
            if inc_i > start_i:
                start_i = inc_i
                end_i = i + 1
        else:
            inc_i = 0

    return sum(L[end_i - start_i:end_i + 1])


longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2])