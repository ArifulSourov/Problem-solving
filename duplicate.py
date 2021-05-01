def finding_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                '''print(arr[i] + "this is duplicate")'''
                return arr[i]

def d_numbers(nums):
    d_numbers = []
    d_numbers.append(nums)
    return d_numbers

 
arr = [3,4,6,8,52,9,6,8,4,54,3]
d = finding_duplicates(arr)
f = d_numbers(d)
print(f)
                
