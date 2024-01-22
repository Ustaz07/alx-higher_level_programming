#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()  # Create a copy of the original list

    if idx < 0 or idx >= len(new_list):
        return new_list  # Return the original list if index is out of range

    new_list[idx] = element  # Replace the element at the specified index
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
