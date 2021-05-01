def calculate_string_len_recursive(input_str, idx=0):
    return calculate_string_len_recursive(input_str, idx+1)

input_str = "rrrrr"
print(calculate_string_len_recursive(input_str, 0))
