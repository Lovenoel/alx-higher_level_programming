#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    if not list_of_integers:  # If the list is empty
        return None
    
    low = 0
    high = len(list_of_integers) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Calculate mid index
        
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]  # Found a peak
        
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:  # Peak is on the left side
            high = mid - 1
            
        else:  # Peak is on the right side
            low = mid + 1
    
    return None  # No peak found
