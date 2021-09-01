from Deque import Deque


def palidrome_checker(input_string):
    char_deque = Deque()

    for char in input_string:
        char_deque.add_rear(char)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal

print(palidrome_checker('lol'))
print(palidrome_checker('lolol'))
print(palidrome_checker('saippuakivikauppias'))
print(palidrome_checker('harry'))