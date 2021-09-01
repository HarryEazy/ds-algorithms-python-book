def bubble_sort_stop(a_list):
    exchanges, pass_num = True, len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        pass_num -= 1
    return a_list


def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        print(pass_num)
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                # print(f'Swapped {a_list[i]} with {a_list[i + 1]}')
    return a_list


def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[position_of_max]:
                position_of_max = location

        a_list[fill_slot], a_list[position_of_max] = a_list[position_of_max], a_list[fill_slot]

    return a_list


# while this is still 0(n**2) shifting requires approx a third of the processing work
# as exchanging since only one assignment is performed, you are only moving index 1 forward
# not switching two values
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value, position = a_list[index], index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position], position = a_list[position - 1], position - 1

        a_list[position] = current_value

    return a_list


def shellSort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:

        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        print("After increments of size", sublist_count,
              "The list is", a_list)

        sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):

        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


# test = [54,26,93,17,77,31,44,55,20]
# shellSort(test)
# print(test)

def mergeSort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging ", a_list)


# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# mergeSort(alist)
# print(alist)


def quickSort(a_list):
    quickSortHelper(a_list, 0, len(a_list) - 1)


def quickSortHelper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quickSortHelper(a_list, first, split_point - 1)
        quickSortHelper(a_list, split_point + 1, last)


def partition(a_list, first, last):
    pivot_value = a_list[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp

    return right_mark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)

# test = [1, 9, 2, 3, 6, 5]
# print(insertion_sort(test))
