def array_advance(A):
    furthest_reached = 0
        last_index = len(A)-1
    i = 0
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, A[i]+i)
        i += 1
    return furthest_reached >= last_index
                      
                      

A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))
B = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(B))

