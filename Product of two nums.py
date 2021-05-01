x = 500
y = 3000

def product_of_two_nums_recursive(x, y):
    if y == 0 or x == 0:
        return 0
    if x < y:
        return y + product_of_two_nums_recursive(x-1, y)
    else:
        return x + product_of_two_nums_recursive(x, y-1)

print(product_of_two_nums_recursive(x, y))
