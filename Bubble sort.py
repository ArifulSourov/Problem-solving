def bubble_sort(elements):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True

        if not swapped:
            break


def bubble_sort_exc(elements, key=None):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True

        if not swapped:
            break

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
elements1 = [1,4,2,7,5,98,56,13]
elements2 = [1,4, 5, 6]
elements3 = ["iory","kyo","benimaru","rugal","terry","gesse"]
bubble_sort(elements1)
print(elements1)
bubble_sort(elements2)
print(elements2)
bubble_sort(elements3)
print(elements3)
bubble_sort_exc(elements, key="transaction_amount")
print(elements)
bubble_sort_exc(elements, key="name")
print(elements)
