from Stack import Stack

def div_by(dec_num):
    if dec_num == 0:
        return 0
    s = Stack()
    
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num


print("hhhh",div_by(242))
    
