#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    data_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = [data_1[x] for x in roman_string] + [0]
    num_val = 0
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i+1]:
            num_val += nums[i]
        else:
            num_val -= nums[i]
    return num_val
