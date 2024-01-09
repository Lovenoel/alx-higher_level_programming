#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None  # Return None if the list is empty

    max_value = my_list[0]  # Initialize max_value with the first element

    for num in my_list[1:]:
        if num > max_value:
            max_value = num  # Update max_value if a larger number is found

    return max_value
