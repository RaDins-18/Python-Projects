# QUESTION:
# Write a python script that can perform binary search on list of elements.



# SOLUTION:

# binary_search() function can return the index of targeted element.
def binary_search(arr, target):
    """
    Performs binary search on a sorted list.

    Args:
        List of elements: A sorted list of elements.
        Target: The element to search for.

    Returns:
        Result: The index of the target element in the list, or -1 if not found.
    """
    # Declare left and right variable with initial values.
    left, right = 0, len(arr) - 1

    # While left variable is less than equal to right variable then run below code.
    while left <= right:
        # Generate the index of an element.
        mid = left + (right - left) // 2

        # If current index element is matched with targeted element then return the index of targeted element.
        if arr[mid] == target:
            # Return index of targeted element.
            return mid
        # If current index element is less than target element then increase the value of left variable.
        elif arr[mid] < target:
            # left variable is equal to (mid variable + 1).
            left = mid + 1
        # If a element is greater than target element then decerease the value of right variable.
        else:
            # right variable is equal to (mid variable - 1).
            right = mid - 1

    # If targeted element is not in the list then return -1.
    return -1

# List of elements.
sorted_list = [1, 3, 5, 7, 9, 11, 13]
# Targeted element.
target_element = 7

# Find the result with the help of binary_search() function.
result = binary_search(sorted_list, target_element)

# If result is not equal to -1 then run below if block code.
if result != -1:
    # Tell user that the targeted element is on that index.
    print(f"Element {target_element} found at index {result}.")
# If result is equal to -1 then run below else block code.
else:
    # Tell user that the targeted element is not in the list.
    print(f"Element {target_element} not found in the list.")

# # Print information about binary_search() function.
# print(help(binary_search))