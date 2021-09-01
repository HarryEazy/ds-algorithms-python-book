from Stack import Stack


# base 2 is binary
# base 16 hex
def base_converter(decimal, base):

    digits = '0123456789ABCDEF'
    remstack = Stack()

    while decimal > 0:
        rem = decimal % base
        remstack.push(rem)
        decimal = decimal // base

    new_string = ''
    while not remstack.is_empty():
        new_string += digits[remstack.pop()]

    return new_string


print(base_converter(15, 16))
