
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(min_index+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if arr[i] != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]



#Test Cases
tests = [
    [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
    [],
    [1,5,8,9],
    [234,3,1,56,34,12,9,12,1300],
    [78, 12, 15, 8, 61, 53, 23, 27],
    [5]
]
for elements in tests:
    selection_sort(elements)
    print(elements)
