def bubble_sort(elements, key):
    size = len(elements)
    # the swapped variable leads to decrease the time complexity of the algorithm
    # to O(n) instead of O(n^2) because in the case that the list is already sorted
    # the algorithm break out of the outer loop
    for rep in range(size-1):
        swapped = False
        for i in range(size - 1 - rep): # I want to stop before the last element
            if elements[i][key] > elements[i+1][key]:
                temp = elements[i+1] # store the next element in a temporary variable
                elements[i+1] = elements[i]
                elements[i] = temp
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    # elements = [1,2,3,5,4]
    # elements = [1,2,3,4,2]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements, 'device')
    print(elements)