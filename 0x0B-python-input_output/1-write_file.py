#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
    - filename (str): The name of the file.
    - text (str): The text to write to the file.

    Returns:
    - int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)

# Test case
if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
