data = [1, 2, 3, 4, 5, 6, 8, 10, 13, 14, 15, 17, 19, 21, 22, 24, 25, 27, 28, 30]
target = 1

#linear Search

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

#Iterative Binary Search

def binary_search_iterative(data, target):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return False

#Recursive Binary Search

def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            return binary_search_recursive(data, target, mid+1, high)
        else:
            return binary_search_recursive(data, target, low, mid-1)
        

print(linear_search(data, target))
print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))
