def get_square_numbers(numbers):
    square_numbers = []
    for n in numbers:
        square_numbers.append(n*n)
    return square_numbers

numbers = [2,6,8,9]
results = get_square_numbers(numbers)
print(results)
