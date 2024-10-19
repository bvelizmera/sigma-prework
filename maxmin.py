numbers = [1, 45, 56, 78, 34, 67, 12, 45]
numbers_2 = [100, -100]


def sort_numbers(nums):
    # This will sort out the numbers in order, returning the max and min by the use of indexes.
    new_nums = sorted(nums)
    return [new_nums[0], new_nums[-1]]


print(sort_numbers(numbers))
print(sort_numbers(numbers_2))
