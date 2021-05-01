class Stack():
    
    def __init__(this):
        this.items = []

    def push(this, item):
        this.items.append(item)

    def pop(this):
        return this.items.pop()

    def is_empty(this):
        return this.items == []

    def peek(this):
        if this.is_empty is not None:
            return this.items[-1]

    def get_stack(this):
        return this.items


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
        
    return rev_str
        



stack = Stack()
input_str = "Hello"
print(reverse_string(stack, input_str))
# print(s.is_empty())
# s.push("A")
# s.push("B")
# print(s.get_stack())
# s.push("C")
# print(s.get_stack())
# s.pop()
# s.pop()
# print(s.get_stack())
# print(s.peek())
# print(s.is_empty())
# print(s.get_stack())
