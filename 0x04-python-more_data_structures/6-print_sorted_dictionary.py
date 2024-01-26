#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)
    for i in sorted_dict:
        print("{}: {}".format(i, a_dictionary[i]))

# Example usage
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
