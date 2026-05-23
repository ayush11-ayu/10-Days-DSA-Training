def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1):

            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]

    print(bubbleSort(arr))