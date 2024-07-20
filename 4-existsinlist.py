def element_exists(lst, element):
    return element in lst

# Example usage:
input_list = [12, 35, 9, 56, 24]
element_to_check = 35

if element_exists(input_list, element_to_check):
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")
