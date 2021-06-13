k = [4, -33, 12, -44, 0.4, 123, 99]


def selectionSort(list):
    for i in range(len(list)):
        minIndex = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]

    return list


def bubbleSort(list):
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


def merge(list, p, q, r):
    n1, n2 = q - p + 1, r - q
    L = [list[i + p] for i in range(n1)]  # Copy left sub-Array to temp arrays L[]
    R = [list[j + q + 1] for j in range(n2)]  # Copy right sub-Array to temp arrays R[]
    y, i, j = p, 0, 0

    for y in range(r):
        if L[i] <= R[j]:
            list[y] = L[i]
            i += 1
        else:
            list[y] = R[j]
            j += 1


def mergeSort(list, p, r):
    if p < r:
        q = (p + (r - 1)) // 2

        mergeSort(list, p, q)
        mergeSort(list, q + 1, r)
        merge(list, p, q, r)


mergeSort(k, 0, len(k))

print(k)
