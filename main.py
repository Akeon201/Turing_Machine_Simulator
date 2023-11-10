"""
Simple Deterministic Finite Automata(DFA) Simulator
Author: Kenyon Leblanc

This project is a personal implementation of a Deterministic Finite Automata(DFA) simulator.

Directions:
Make sure you are in the directory of "main.py". Start the program by typing "python main.py" or "python3 main.py".

At anytime, you may type "exit" to quit the program.

You will be prompted for a filename, please make sure to include the extension.
If not file is not found, you will be prompted to try again.

The file must be formatted in this specific format:
    Line 1: The first line of your file will be a single integer that indicates how many states the DFA contains.
    A note about states: States are represented by consecutive integers starting from zero. State zero is
    always the start state. All states of the DFA must be represented; this includes the dead state.

    Line 2: The second line of the file contains a space-separated list of integers that represent accepting
    states.

    Line 3: Alphabet: a space-separated list of characters in the DFA's alphabet.

    Lines 4 – end: Transitions: These will be represented in a table indexed by state number and character.
    The input file will have one line for each row of the table. Each row consists of integers that represent the
    states the machine will transition to on each of the alphabet characters. If the DFA has seven states and
    three characters, there will be seven lines containing three integers each. The first row corresponding to
    the transitions from state zero, the second from state one, etc. Note that all transitions must be
    represented; do not assume a missing transition for a character is to the dead state.

You will be prompted for a string to be inputted into the DFA.
If an invalid character is found, it will be displayed along with a list of valid characters.

If all input is valid, the process of iterating through the string will be shown.
{e} will be they symbol for the empty string.
At the end of the DFA computation will be an ACCEPTED or REJECTED.
ACCEPTED means that the processed string ended in an accepting state.
REJECTED means that the processed string ended in a dead state.

You will be continually asked for an input string until "exit" is entered.
"""

import os  # Check directory files

# Initialize global lists
state_table = []
halt_states = []
alphabet = []


def check_valid_file(file_name):
    """
    Check if file provided by user input is valid.
    :param file_name: file name w/ extension
    :return: valid file name
    """
    # Current directory
    directory = os.getcwd()
    # List of files from cwd
    listed_directory = os.listdir(directory)
    # Continue loop until valid file name is given
    while file_name not in listed_directory:
        print("File not found, please try again.")
        file_name = input("Please enter file name with extension: ")
        check_exit_command(file_name)

    return file_name


def load_file(file_name):
    """
    Load data from file into global variables.
    :param file_name: Name of file
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Store line 2 into accepted states list
    halt_states.extend(list(lines[1].split()))

    # Store alphabet into alphabet list. Iterate through all lines 1 onward to check for all characters.
    for line in lines[1:]:
        characters = line.split()[1:2]
        for char in characters:
            if char not in alphabet:
                alphabet.extend(characters)

    if '_' not in alphabet:
        alphabet.extend('_')

    # Store remaining lines from 2 onward into state table
    for line in lines[2:]:
        values = list(line.split())
        state_table.append(values)


def check_string_input(user_input):
    """
    Check all elements in string are in defined alphabet.
    :param user_input: String from user input
    :return: Returns a valid string
    """
    comma = ","
    list_alphabet = comma.join(alphabet)
    check = -1

    while check != 1:
        check = check + 1
        for char in user_input:
            if char not in alphabet:
                print(f"REJECTED")
                print(f"Found invalid character {char}")
                print(f"Valid characters are {list_alphabet}")
                user_input = input("Please enter a string to evaluate: ")
                check_exit_command(user_input)
                check = check - 1
                break

    if user_input[0] != '_':
        user_input = '_'+user_input
    if user_input[-1] != '_':
        user_input = user_input + '_'

    return user_input


def turing_logic(input_string):
    """
    Turing machine logic
    :param input_string: string to be tested
    """
    input_string = list(input_string)
    current_pos = 0
    current_state = '0'

    print('[Start]')
    temp_string = input_string.copy()
    temp_string[current_pos] = add_brackets(temp_string[current_pos])
    print(''.join(temp_string))

    while current_state not in halt_states:
        for row in state_table:
            if row[0] == current_state and row[1] == input_string[current_pos]:
                input_string[current_pos] = row[2]
                current_pos = current_pos+move(row[3])
                temp_string = input_string.copy()
                temp_string[current_pos] = add_brackets(temp_string[current_pos])
                print(''.join(temp_string))
                current_state = row[4]
                break
    print('[Halt]')


def move(character):
    """
    Checks if character is L or R
    :param character: L or R
    :return: -1 or 1
    """
    if character == 'R':
        return 1
    else:
        return -1


def add_brackets(character):
    """
    Add brackets to character or string
    :param character: any character or string
    :return: modified string with added brackets
    """
    new_string = '['+character+']'
    return new_string


def check_exit_command(string):
    """
    Check if string reads "exit". If so, exit gracefully.
    :param string:
    """
    if string == "exit":
        print("Closing...")
        exit(0)


if __name__ == '__main__':

    print("Type 'exit' at anytime to quit.")

    # Gather file names and load file
    file_name = input("Please enter file name with extension: ")
    check_exit_command(file_name)
    file_name = check_valid_file(file_name)
    print("Loading...")
    load_file(file_name)

    # Infinite loop so that the user may input as many string inputs as they want.
    while 1:
        user_input = input("Please enter a string to evaluate (including '_' is optional): ")
        check_exit_command(user_input)
        user_input = check_string_input(user_input)

        turing_logic(user_input)
