
def quick_sort(elements, left_pointer, right_pointer):

    if len(elements) == 1:
        return


    if left_pointer < right_pointer:

        pivot_idx = partition(elements, left_pointer, right_pointer)
        quick_sort(elements, left_pointer, pivot_idx - 1)
        quick_sort(elements, pivot_idx + 1, right_pointer)

def swap(elements, left_pointer, right_pointer):

    if right_pointer != left_pointer:
        temp = elements[right_pointer]
        elements[right_pointer] = elements[left_pointer]
        elements[left_pointer] = temp

def partition(elements, left_pointer, right_pointer):

    pivot = elements[right_pointer]
    p_index = left_pointer

    for i in range(left_pointer, right_pointer):
        # when the element is > pivot we do not enter the loop 
        # this way the p_index stays put and then we increase i until we find 
        # an element that is less than pivot
        if elements[i] <= pivot:
            swap(elements, p_index, i)
            p_index += 1
    swap(elements, p_index, right_pointer)
    return p_index            


if __name__=='__main__':

    # elements = [11,9,29,7,2,15,28]
    # # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    # quick_sort(elements, 0, len(elements) - 1)
    # print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')