"""
Given an array of integers, every element appears twice except for one. Find
that single one.

Note: Algo should have a linear runtime complexity.

Input: [1, 2, 2, 3, 1]
Output: 3

"""

arr = [1, 2, 2, 3, 1]
def single_number(arr):
    ans = 0
    for i in range(len(arr)):
        ans ^= arr[i]
    return ans


def single_num(arr):
    temp = {}
    for i in arr:
        if i not in temp:
            temp[i] = 1
        else:
            del temp[i]

    return list(temp.keys())[0]
            
        
        
            
        
        
#print(single_number(arr))
print(single_num(arr))
    
