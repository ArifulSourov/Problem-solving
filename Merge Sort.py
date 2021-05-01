def merge_two_sorted_array(a, b, arr):
    #sorted_array = []
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            #sorted_array.append(a[i])
            i += 1
        else:
            arr[k] = b[j]
            #sorted_array.append(b[j])
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        #sorted_array.append(a[i])
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        #sorted_array.append(b[j])
        j += 1
        k += 1

    #return sorted_array


def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_array(left, right, arr)




test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]


for arr in test_cases:
    merge_sort(arr)
    print(arr)
        

    
