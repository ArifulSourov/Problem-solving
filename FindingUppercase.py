#Given a string, find the first uppercase character in both iterqative and recursive way
input_str_1 = "likeItornot"
input_str_2 = "LikeitorNot"
input_str_3 = "likeitornot"


# Iterative way
def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character"

# recursive way
def find_uppercase_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str)-1:
        return "No uppercase character"
    return find_uppercase_recursive(input_str, idx+1)


print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))
            
print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))
