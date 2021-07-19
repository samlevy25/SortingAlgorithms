#k = [4, -33, 12, -44, 4, 13, 11]
k = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]


def selectionSort(list):  # Θ(𝑛^2)
    for i in range(len(list)):
        minIndex = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]

    return list


def bubbleSort(list):  # Θ(𝑛^2)
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j + 1] < list[j]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def insertionSort(list):  # Θ(𝑛^2)
    for i in range(1, len(list)):
        key, j = list[i], i - 1
        while list[j] > key and j >= 0:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list


def partition(arr, p, r):  # Θ(𝑛)
    i, x = p - 1, arr[r]  # x is pivot

    for j in range(p, r):
        if arr[j] <= x:  # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quickSort(arr, p, r):  # Θ(𝑛^2)
    if len(arr) == 1:
        return arr

    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)

    return arr


def countingSorting(arr):  # Θ(n + k)

    max_, min_ = max(arr), min(arr)
    countArr = [0] * (max_ - min_ + 1)
    outputArr = [0] * (len(arr))

    for i in range(0, len(arr)):
        countArr[arr[i] - min_] += 1

    for j in range(1, len(countArr)):
        countArr[j] += countArr[j - 1]

    for x in range(len(arr) - 1, -1, -1):
        outputArr[countArr[arr[x] - min_] - 1] = arr[x]
        countArr[arr[x] - min_] -= 1

    for t in range(0, len(arr)):
        arr[t] = outputArr[t]

    return arr




