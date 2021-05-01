def removeDup(l1):
    N = len(l1)
    i = j = 1
    if N <= 1: return N
    while i < N:
        if l1[i] !=  l1[i-1]:
            l1[j] = l1[i]
            j += 1
        i += 1
    return j

l1 = [1,1,2,2,3,4,5,6,6]
print(removeDup(l1))
