j = 0
arr = [1,1,1,3,3,4,5,6,7,7,8,8,9,9,9]
length = len(arr)
count = 0
for i  in range(0, length-1):
    if (arr[i] != arr[i+1]):
        arr[j+1] = arr[i+1]
        j = j+1

#j=j+1
arr[j] = arr[length - 1]
for k in range(0, j+1):
    print(arr[k])
    
