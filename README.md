# Turing_Machine_Simulator
#### Author: Kenyon Leblanc
This project is a personal implementation of a Deterministic Finite Automata(DFA) simulator.

## Directions

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
