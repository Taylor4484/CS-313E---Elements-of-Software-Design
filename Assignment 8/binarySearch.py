def binarySearch(lst, x, lo, hi):
    """This implements a binary search for x on a
    list lst, between indices lo and hi.  The index
    is returned if x is found, else -1 is returned."""
    comparisons = 0
    while lo < hi:
        comparisons += 1
        mid = (lo + hi)//2
        midval = lst[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return (mid, comparisons)
    return (-1, comparisons)

