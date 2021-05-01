input_str = "Loveme like you do"
print(len(input_str))

def iterative_str_len(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])


print(recursive_str_len(input_str))
print(iterative_str_len(input_str))
