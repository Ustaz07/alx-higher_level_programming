#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None and isinstance(a_dictionary, dict):
        for key in sorted(a_dictionary.keys()):
            print("{}: {}".format(key, a_dictionary[key]))

# Example usage
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
