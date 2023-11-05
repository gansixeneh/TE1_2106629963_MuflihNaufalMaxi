import time
from random import randint
from memory_profiler import memory_usage

block = [0] * 1024
B = 1024

def merge(arr1, arr2):
    i = j = 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

def MergeSort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    left_result = MergeSort(A[:mid])
    right_result = MergeSort(A[mid:])
    return merge(left_result, right_result)

def partition(A, l, r):
    n = r-l
    p = A[l]
    q = A[r-1]
    i = j = k = l+1
    num_p = num_q = 0
    while k < r-1:
        t = min(B, r-1-k)
        for c in range(t):
            block[num_q] = c
            num_q += (q >= A[k+c])
        for c in range(num_q):
            A[j+c], A[k+block[c]] = A[k+block[c]], A[j+c]
        k += t
        for c in range(num_q):
            block[num_p] = c
            num_p += (p > A[j+c])
        for c in range(num_p):
            A[i], A[j+block[c]] = A[j+block[c]], A[i]
            i += 1
        j += num_q
        num_p = num_q = 0
    A[i-1], A[l] = A[l], A[i-1]
    A[j], A[r-1] = A[r-1], A[j]
    return (i-1, j)


def TwoPivotQuicksort(A, l=None, r=None):
    if l is None:
        l, r = 0, len(A)
        A = A.copy()

    rec_stack = [(l, r)]

    while len(rec_stack) > 0:
        l, r = rec_stack.pop()

        if r-l <= 1:
            continue

        if A[l] > A[r-1]:
           A[l], A[r-1] = A[r-1], A[l]

        i, j = partition(A, l, r)

        rec_stack.append((l, i))
        rec_stack.append((i+1, j))
        rec_stack.append((j+1, r))

    return A

def display_total_memory(sorting_func, A):
    memory_usages = memory_usage((display_total_running_time, (sorting_func, A)), max_iterations=1)
    print(f"Total memori yang digunakan: {max(memory_usages)} MB")

def display_total_running_time(sorting_func, A):
    start_time = time.time()
    print(f"Waktu sorting dimulai: {start_time}")
    sorting_func(A) 
    end_time = time.time()
    print(f"Waktu sorting selesai: {end_time}")
    print(f'Total waktu: {(end_time - start_time) * 1000} ms')

def find_total_memory(A):
    print("-------------- Two Pivot Quicksort --------------")
    display_total_memory(TwoPivotQuicksort, A)
    print()

    print("------------------- Merge Sort -------------------")
    display_total_memory(MergeSort, A)
    print()
    print()

if __name__ == '__main__':
    for p in [9, 13, 16]:

        print("============================================================")

        print("Status array: sorted")
        print(f"Ukuran array: 2^{p}\n\n")
        arr_size = 2**p
        A = [i for i in range(arr_size)]

        find_total_memory(A)

        print("Status array: random")
        print(f"Ukuran array: 2^{p}\n\n")
        arr_size = 2**p
        A = [randint(-1000000, 1000000) for i in range(arr_size)]

        find_total_memory(A)

        print("Status array: reversed")
        print(f"Ukuran array: 2^{p}\n\n")
        arr_size = 2**p
        A = [-i for i in range(arr_size)]

        find_total_memory(A)