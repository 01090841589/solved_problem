def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for size in range(len(x)-1, -1, -1):
        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)

def selectionSort(x):
    for size in range(len(x)-1, -1, -1):
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
        swap(x, max_i, size)

def insertionSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val

def gapInsertionSort(x, start, gap):
    for target in range(start+gap, len(x), gap):
        val = x[target]
        i = target
        while i > start:
            if x[i-gap] > val:
                x[i] = x[i-gap]
            else:
                break
            i -= gap
        x[i] = val

def shellSort(x):
    gap = len(x) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(x, start, gap)
        gap = gap // 2



def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]



def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1
    swap(x, pivot_idx, rmark)
    return rmark

def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotMethod(x, first, last)
            _qsort(x, first, splitpoint-1)
            _qsort(x, splitpoint+1, last)
    _qsort(x, 0, len(x)-1)




number = [5, 3, 1, 6, 3, 2, 5, 2, 23, 14]

# bubbleSort(number)
# selectionSort(number)
# insertionSort(number)
# shellSort(number)
mergeSort(number)
# quickSort(number)


print(number)
