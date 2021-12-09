# Author: Elliott Larsen
# Date:
# Description: 


class HasamiShogiGame:
    """
    Represents a Hasami Shogi class.  All data members of this class are set to private and getter/setter methods
    are used to update and access the data members.
    """

    def __init__(self):
        """
        Creates a new Hasami Shogi Game.  All data members are set to private.
        """

        self._current_board = [[" ", 1, 2, 3, 4, 5, 6, 7, 8, 9], ["a", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
        ["b", ".", ".", ".", ".", ".", ".", ".", ".", "."], ["c", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["d", ".", ".", ".", ".", ".", ".", ".", ".", "."], ["e", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["f", ".", ".", ".", ".", ".", ".", ".", ".", "."], ["g", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["h", ".", ".", ".", ".", ".", ".", ".", ".", "."], ["i", "B", "B", "B", "B", "B", "B", "B", "B", "B"]]
        self._current_state = "UNFINISHED"
        self._active_player = "BLUE"
        self._captured_blue_pieces = 0
        self._captured_orange_pieces = 0
        self._invalid_message = "Invalid Entry"

    def print_board(self):
        """
        Prints the board.
        """

        for row in self._current_board:
            for column in row:
                print(column, end = " ")
            print()

    def get_game_state(self):
        """
        Returns the current state of the game (UNFINISHED, BLUE_WON, or ORANGE_WON)
        """

        return self._current_state
    
    def set_game_state(self, condition):
        """
        Takes one of the three conditions (UNFINISHED, BLUE_WON, or ORANGE_WON) as a parameter and updates the 
        current game state accordingly.
        """

        condition = condition.lower()

        if condition == "unfinished":
            self._current_state = "UNFINISHED"
        elif condition == "blue_won":
            self._current_state = "BLUE_WON"
        elif condition == "orange_won":
            self._current_state = "ORANGE_WON"
        else:
            return self._invalid_message
    
    def get_active_player(self):
        """
        Returns whose turn it is.
        """

        return self._active_player

    def switch_active_player(self):
        """
        This is essentially a setter method for self._active_player.  When this method is called, it updates
        changes the turn.
        """

        if self.get_active_player() == "BLUE":
            self._active_player = "ORANGE"
        else:
            self._active_player = "BLUE"

    def get_enemy_player(self):
        """
        Returns the enemy player.
        """

        if self.get_active_player() == "BLUE":
            return "ORANGE"
        else:
            return "BLUE"

    def get_friendly_piece_color(self):
        """
        Returns a letter that corresponds to the color of the friendly piece.
        """

        if self.get_active_player() == "BLUE":
            return "B"
        else:
            return "O"

    def get_enemy_piece_color(self):
        """
        Returns a letter that corresponds to the color of the friendly piece.
        """

        if self.get_active_player() == "BLUE":
            return "O"
        else:
            return "B"

    def get_num_captured_pieces(self, piece_color):
        """
        Takes the color of a piece as a paramter and returns how many pieces of that color have been captured.
        """

        piece_color = piece_color.lower()

        if piece_color == "blue" or piece_color == "b":
            return self._captured_blue_pieces
        elif piece_color == "orange" or piece_color == "o":
            return self._captured_orange_pieces
        else:
            return self._invalid_message
    
    def set_num_captured_pieces(self, piece_color):
        """
        Takes the color of a piece as a parameter and increments the number of captured pieces by 1.
        """

        piece_color = piece_color.lower()

        if piece_color == "blue" or piece_color == "b":
            self._captured_blue_pieces += 1
        elif piece_color == "orange" or piece_color == "o":
            self._captured_orange_pieces += 1
        else:
            return self._invalid_message


