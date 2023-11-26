# Turing Machine Simulator
#### Author: Kenyon Leblanc
This project is a personal implementation of a Turing Machine Simulator.

## Directions

    Make sure you are in the directory of "main.py". Start the program by typing "python main.py" or "python3 main.py".
    
    At anytime, you may type "exit" to quit the program.
    
    You will be prompted for a filename, please make sure to include the extension.
    If not file is not found, you will be prompted to try again.
    
    The file must be formatted in this specific format:

        Line 1: The first line of your file will be a single integer that indicates how many states the TM contains. States are
        represented by consecutive integers starting from zero. State zero is always the start state.
        
        Line 2: The second line contains the number of the halting state.
        
        Line 3: The remaining lines represent the transitions. These will be stored in a table indexed by state number and
        character. The input file will have one line for each row of the table. Each row represents one transition,
        indicating the character to write on the current cell, the direction to move the read‐write head, and the
        state to transition to. Blank cells will be represented using an underscore ( _ ).

    You will be prompted for a string.
    If an invalid character is found, it will be displayed along with a list of valid characters.
    
    If all input is valid, the process of iterating through the string will be shown.
    [Start] means the turing machine is beginning in the start state.
    [Halt] means the turing machine has reached a halt state.
    
    You will be continually asked for an input string until "exit" is entered.
