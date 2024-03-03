def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    while True:
        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
            left_child = 2 * i + 1
            right_child = 2 * i + 2
        else:
            break

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7, -1, 4, 3, 0, 0, 8, -42, 9, 38]

    print("Original array:", arr)

    heap_sort(arr)

    print("Sorted array:", arr)
