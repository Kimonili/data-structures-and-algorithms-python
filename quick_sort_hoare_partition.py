def quick_sort(elements, left_pointer, right_pointer):
    if left_pointer < right_pointer:
        partition_idx = partition(elements, left_pointer, right_pointer)
        quick_sort(elements, left_pointer, partition_idx - 1)
        quick_sort(elements, partition_idx + 1, right_pointer)


def swap(elements, left_pointer, right_pointer):
    temp = elements[right_pointer]
    elements[right_pointer] = elements[left_pointer]
    elements[left_pointer] = temp

def partition(elements, left_pointer, right_pointer):

    if len(elements) <= 1:
        return elements
    
    pivot_idx = left_pointer
    pivot = elements[pivot_idx]

    while left_pointer < right_pointer:

        while left_pointer < len(elements) and elements[left_pointer] <= pivot:
            left_pointer += 1
        
        while elements[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer < right_pointer:
            swap(elements, left_pointer, right_pointer)

    swap(elements, pivot_idx, right_pointer)

    return right_pointer

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)

    # tests = [
    #     [11,9,29,7,2,15,28],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]]

    # for elements in tests:
    #     quick_sort(elements, 0, len(elements)-1)
    #     print(f'sorted array: {elements}')