
def linear_search(numbers_list, number_to_find):
	for idx, value in enumerate(numbers_list):
		if value == number_to_find:
			return idx
		return -1

def binary_search(numbers_list, number_to_find):
	left_idx = 0
	right_idx = len(numbers_list) - 1 # because it starts from zero
	middle_idx = 0

	while left_idx <= right_idx:
		middle_idx = (left_idx + right_idx) // 2
		middle_number = numbers_list[middle_idx]

		if number_to_find == middle_number:
			return middle_idx

		if number_to_find < middle_number:
			right_idx = middle_idx - 1
		else:
			left_idx = middle_idx + 1

	return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def find_occurances(numbers_list, number_to_find):
	index = binary_search_recursive(numbers_list, number_to_find, left_index=0, right_index=len(numbers_list)-1)
	occurances = [index]

	i = index - 1
	while i >= 0:
		occurance = binary_search_recursive(numbers_list, number_to_find, left_index=0, right_index=i)
		if occurance != -1:
			occurances.append(occurance)
		i = i - 1

	i = index + 1
	while i <= len(numbers_list) - 1:
		occurance = binary_search_recursive(numbers_list, number_to_find, left_index=i, right_index=len(numbers_list) - 1)
		if occurance != -1:
			occurances.append(occurance)
		i = i + 1
	
	return occurances


if __name__ == '__main__':
	numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
	number_to_find = 15
	index = find_occurances(numbers_list, number_to_find)
	print(f"Number found at index {index} using binary search")
