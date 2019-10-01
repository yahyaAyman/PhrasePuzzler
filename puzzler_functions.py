"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Compares the view with the puzzle returning true if they both match.
    >>> is_win('banana', 'banana')
    True
    >>> is_win('banana', 'bana^a')
    False
    >>> is_win('banana', 'ba^ana')
    False
    """
    return puzzle == view

def game_over(puzzle: str, view: str, selection: str) -> bool:
    """Compares the puzzle to the view or if the selection is QUIT.
    >>> game_over( 'banana', 'banan^', 'S')
    False
    >>> game_over( 'banana', 'banana', 'Q')
    True
    >>> game_over( 'banana', 'banan^', 'Q')
    True
    """
    if is_win(puzzle, view) or selection == QUIT:
        return True
    return False

def bonus_letter(puzzle: str, view: str, letter: str)-> bool:
    """ Evaluates the puzzle, its view, and the letter. If the letter is in
    the puzzle and not in the view update the view
    >>> bonus_letter('cat' , '^at', 'c')
    True
    >>> bonus_letter('cat', 'cat', 'c')
    False
    >>> bonus_letter('cat', 'c^t', 'f')
    False
    """

    if letter is not ('a' or 'e' or 'i' or 'u' or 'o'):
        if (letter in puzzle) and (letter not in view):
            return True
    return False


def update_letter_view(puzzle: str, view: str, index: int, letter_guessed: str)-> str:
    """The character in the index of the puzzle should
        matches the guess to return that character
    >>> update_letter_view('banana', '^anana', 0, 'b')
    "b"
    >>> update_letter_view('banana', '^anana', 0, 'f')
    "^"
    >>> update_letter_view('banana', 'ba^a^a', 2, 'n')
    'n'
    """
    if letter_guessed in puzzle[index]:
        return letter_guessed
    return view[index]

def calculate_score(current_score: int,\
                    number_of_letter_occurrences: int, vowel_consonent: str)-> int:
    """Calculates the score according to player entries
       >>> calculate_score(5,2, VOWEL)
       4
       >>> calculate_score(5,6,CONSONANT)
       11
       >>> calculate_score(3,2,VOWEL)
       2
       """
    if vowel_consonent == CONSONANT:
        return current_score + (number_of_letter_occurrences * CONSONANT_POINTS)
    else:
        return current_score - VOWEL_PRICE



def next_player(current_player: str, number_of_occurrences: int)-> str:
    """When the number of occurrences is more than zero then current_player plays again
    if it is zero the other player gets the turn.
    >>>next_player( PLAYER_TWO, 0)
    'Player One'
    >>> next_player(PLAYER_ONE, 2)
    'Player One'
    >>> next_player(PLAYER_TWO, 2)
    'Player Two'
    """
    if number_of_occurrences > 0:
        return current_player
    else:
        if current_player == PLAYER_ONE:
            return PLAYER_TWO
        else:
            return PLAYER_ONE


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
