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

        self._current_board = [[" ", 1, 2, 3, 4, 5, 6, 7, 8, 9], ["a", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
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

    def get_square_occupant(self, coord):
        """
        Takes a coordinate as a parameter and returns the current occupant (if any) of the square.  
        """

        coord = list(coord)
        temp_list = []        
        occupant = ""
        x_coord = ""

        for i in coord[1:]:
            temp_list.append(i)
        for j in temp_list:
            x_coord += j
        
        x_coord = int(x_coord)
        y_coord = coord[0].lower()

        for row in self._current_board:
            if row[0] == y_coord:
                occupant = row[x_coord]

        if occupant.lower() == "b":
            return "BLUE"
        elif occupant.lower() == "o":
            return "ORANGE" 
        else:
            return "NONE"  

    def set_square_occupant(self, coord, new_condition):
        """
        Takes the coordinate and new condition as parameters.  It will update the board based on the parameter 
        passed to it.  For instance, if "e3, "B" are given as parameters, then e3 will be changed to B.
        """   

        coord = list(coord)
        temp_list = []
        x_coord = ""

        for i in coord[1:]:
            temp_list.append(i)
        for j in temp_list:
            x_coord += j

        x_coord = int(x_coord)
        y_coord = coord[0].lower()

        for row in self._current_board:
            if row[0] == y_coord:
                row[x_coord] = new_condition 

    def slice_coord(self, old_coord, new_coord):
        """
        Takes old and new coordinates and slices them into characters and integers.  This method returns a list 
        consisting of x axis index of the coordinates (numeric representation) and y axis index of the 
        coordinates (both character and numeric representations), which will be used by other methods.
        """

        old_coord = list(old_coord)
        new_coord = list(new_coord)
        row_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        old_x_coord_list = []
        new_x_coord_list = []
        old_x_coord = ""
        new_x_coord = ""
    

        for i in old_coord[1:]:
            old_x_coord_list.append(i)
        for j in old_x_coord_list:
            old_x_coord += j

        old_x_coord = int(old_x_coord)
        old_y_coord = old_coord[0].lower()

        for j in new_coord[1:]:
            new_x_coord_list.append(j)
        for k in new_x_coord_list:
            new_x_coord += k
        
        new_x_coord = int(new_x_coord)
        new_y_coord = new_coord[0].lower()

        if old_y_coord in row_char:
            old_y_index = row_char.index(old_y_coord)
        else:
            old_y_index = None

        if new_y_coord in row_char:
            new_y_index = row_char.index(new_y_coord)
        else:
            new_y_index = None

        return [old_x_coord, old_y_coord, old_y_index, new_x_coord, new_y_coord, new_y_index]


