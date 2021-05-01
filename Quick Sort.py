elements = [23, 1, 4, 33, 14, 7, 11, 30]

def quick_sort(elements, start, end):
    if start < end:
        pi = partion(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)



def partion(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end

def partition_lomuto(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)

    return p_index

def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    

quick_sort(elements, 0, len(elements)-1)
print(elements)

tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

for elements in tests:
    quick_sort(elements, 0, len(elements)-1)
    print(f'sorted array: {elements}')
