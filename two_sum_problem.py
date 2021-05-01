def two_sum_brute_force(A, target):
    for i in range(len(A)-1):
        for j in range(1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False

def two_sum_hash_table(A, target):
    h = dict()
    for i in range(len(A)):
        if A[i] in h:
            print(h[A[i]], A[i])
            return True
        else:
            h[target - A[i]] = A[i]
    return False

def two_sum(A, target):
    i = 0
    j = len(A) - 1
    for i in range(len(A)-1):
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False

A = [1, 2, 3, 4, 11]
print(two_sum_brute_force(A, 13))
print(two_sum_hash_table(A, 13))
print(two_sum(A, 13))
