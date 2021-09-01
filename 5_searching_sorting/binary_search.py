def binary_search(a_list, item):
    start, end, found = 0, len(a_list) - 1, False

    while start <= end and not found:
        mid = (start + end) // 2
        if a_list[mid] == item:
            found = True
        else:
            if item < a_list[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return found


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        mid = len(a_list) // 2
        if a_list[mid] == item:
            return True
        else:
            if item < a_list[mid]:
                return binary_search_recursive(a_list[:mid], item)
            else:
                return binary_search_recursive(a_list[mid + 1:, item])
