# Author: Elliott Larsen
# Date:
# Description: This is a console version of Hasami Shogi.  Please see README.md for more details of the program
#              and rules of the game.


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
        self._blue_won_MSG = "Blue won.  Goodbye!"
        self._orange_won_MSG = "Orange won.  Goodbye!"

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
        Takes the color of a piece as a parameter and returns how many pieces of that color have been captured.
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

    def is_skipping_turn(self, old_coord, new_coord):
        """
        Takes the old and new coordinates as parameters and checks if the two coordinates are identical.  
        If so, it returns True.  Otherwise, it returns False.
        """

        if old_coord == new_coord:
            return True
        else:
            return False

    def is_outside_board(self, old_coord, new_coord):
        """
        Takes old and new coordinates as parameters and checks if the piece is trying to move to or from
        a place that is not inside the board.  If so, it returns True.  If both locations are within the
        board, it returns False.
        """

        coord = self.slice_coord(old_coord, new_coord)
        if coord[0] > 9 or coord[1] > "i":
            return True
        elif coord[3] > 9 or coord[4] > "i":
            return True
        else:
            return False

    def is_wrong_turn(self, old_coord):
        """
        Takes the old coordinate as a parameter and checks if the current player's piece is not in
        the old coordinate.  If so, the player is trying to move a piece that does not belong to
        them and it returns True.  Otherwise, it returns False.
        """

        if self.get_active_player() == "BLUE":
            if self.get_square_occupant(old_coord) != "BLUE":
                return True
        if self.get_active_player() == "ORANGE":
            if self.get_square_occupant(old_coord) != "ORANGE":
                return True
        
        return False

    def is_diagonal_move(self, old_coord, new_coord):
        """
        Takes old and new coordinates as parameters and checks if the proposed move is diagonal.  If so,
        it returns True.  If not, it returns False.
        """

        coord = self.slice_coord(old_coord, new_coord)

        if coord[0] != coord[3] and coord[1] != coord[4]:
            return True
        else:
            return False

    def is_won(self):
        """
        When this method is called, it will check the number of captured pieces for each color
        and update the current game status accordingly.  It will return True if the game is won
        and will return False otherwise.
        """

        if self.get_num_captured_pieces("BLUE") >= 8:
            self.set_game_state("orange_won")
            return True

        elif self.get_num_captured_pieces("ORANGE") >= 8:
            self.set_game_state("blue_won")
            return True

        else:
            self.set_game_state("unfinished")
            return False

    
    def is_jumping(self, old_coord, new_coord):
        """
        Takes old and new coordinates as parameters and determines if the proposed move jumps over any piece on
        the board.  If the move results in a jump, it will return True.  Otherwise, it will return False.
        """

        coord = self.slice_coord(old_coord, new_coord)

        # horizontal jump
        if coord[1] == coord[4] and coord[0] < coord[3]:
            for i in self._current_board:
                if i[0] == coord[1]:
                    for j in i[coord[0] + 1 : coord[3]]:
                        if j != ".":
                            return True
                    else:
                        return False

        elif coord[1] == coord[4] and coord[0] > coord[3]:
            for i in self._current_board:
                if i[0] == coord[1]:
                    for j in i[coord[3] + 1 : coord[0]]:
                        if j != ".":
                            return True
                    else:
                        return False

        # vertical jump
        elif coord[0] == coord[3] and coord[2] < coord[5]:
            for i in self._current_board[coord[2] + 2 : coord[5] + 1]:
                if i[coord[3]] != ".":
                    return True
            else:
                return False

        elif coord[0] == coord[3] and coord[2] > coord[5]:
            for i in range(coord[5] + 2, coord[2] + 1):
                if self._current_board[i][coord[3]] != ".":
                    return True
            else:
                return False
        else:
            return False

    def is_captured(self, old_coord, new_coord):
        """
        Takes old and new coordinates as parameters and determines if the proposed move results in any capture 
        by the current player.  It will call five methods that check all four directions plus four corners.
        Within each method, if the move constitutes a capture, it will increment the number of captured pieces
        and remove the captured pieces from the board.
        """

        self.scan_left(old_coord, new_coord)
        self.scan_right(old_coord, new_coord)
        self.scan_above(old_coord, new_coord)
        self.scan_below(old_coord, new_coord)
        self.scan_corners(old_coord, new_coord)

    def scan_left(self, old_coord, new_coord):
        """
        Takes old and new coordinates as parameters.  After a piece is moved to a new location, it scans for any 
        potential captures to the left of the new square.  If there is any captured pieces, it updates the number
        of captured pieces and removes the captured pieces.
        """
        
        coord = self.slice_coord(old_coord, new_coord)
        enemy_piece = self.get_enemy_piece_color()
        friendly_piece = self.get_friendly_piece_color()
        counter = 0

        for i in self._current_board:
            if i[0] == coord[4]:
                for j in i[coord[3] - 1 : 0 : -1]:
                    if j != friendly_piece:
                        counter += 1
                        continue
                    else:
                        counter += 1
                        index = int(coord[3] - counter)
                        for k in i[index + 1 : coord[3]]:
                            if k == ".":
                                break
                        else:
                            for k in i[index + 1: coord[3]]:
                                if k == enemy_piece:
                                    self.set_num_captured_pieces(enemy_piece)
                                    i[index + 1] = "."
                                    index += 1
                        break

    def scan_right(self, old_coord, new_coord):
        """
        Takes old and new coordinates as parameters.  After a piece is moved to a new location, it scans for any 
        potential captures to the right of the new square.  If there is any captured pieces, it updates the 
        number of captured pieces and removes the captured pieces.
        """

        coord = self.slice_coord(old_coord, new_coord)
        enemy_piece = self.get_enemy_piece_color()
        friendly_piece = self.get_friendly_piece_color()
        counter = 0

        for i in self._current_board:
            if i[0] == coord[4]:
                for j in i[coord[3] + 1 : ]:
                    if j != friendly_piece:
                        counter += 1
                        continue
                    else:
                        counter += 1
                        index = int(coord[3] + counter)
                        for k in i[coord[3] + 1 : index]:
                            if k == ".":
                                break
                        else:
                            new_x_coord = coord[3] + 1
                            for k in i[new_x_coord: index]:
                                if k == enemy_piece:
                                    self.set_num_captured_pieces(enemy_piece)
                                    i[new_x_coord] = "."
                                    new_x_coord += 1
                        break

    def scan_above(self, old_coord, new_coord):
        """
        Takes old and new coordinates as parameters.  After a piece is moved to a new location, it scans for any 
        potential captures to the north of the new square.  If there is any captured pieces, it updates the 
        number of captured pieces and removes the captured pieces.
        """

        coord = self.slice_coord(old_coord, new_coord)
        enemy_piece = self.get_enemy_piece_color()
        friendly_piece = self.get_friendly_piece_color()
        counter = 0

        for i in self._current_board[coord[5] : 0 : -1]:
            if i[coord[3]] != friendly_piece:
                counter += 1
                continue
            else:
                counter += 1
                new_y_index = coord[5]
                for num in range(counter):
                    if self._current_board[new_y_index][coord[3]] == ".":
                        return False
                    else:
                        new_y_index -= 1
                        continue

                new_y_index = coord[5]
                for num in range(counter):
                    if self._current_board[new_y_index][coord[3]] == enemy_piece:
                        self.set_num_captured_pieces(enemy_piece)
                        self._current_board[new_y_index][coord[3]] = "."
                        new_y_index -= 1
                        continue
                break

    def scan_below(self, old_coord, new_coord):
        """
        Takes old and new coordinates as parameters.  After a piece is moved to a new location, it scans for any
        potential captures to the south of the new square.  If there is any captured pieces, it updates the 
        number of captured pieces and removes the captured pieces.
        """

        coord = self.slice_coord(old_coord, new_coord)
        enemy_piece = self.get_enemy_piece_color()
        friendly_piece = self.get_friendly_piece_color()
        counter = 0

        for i in self._current_board[coord[5] + 2:]:
            if i[coord[3]] != friendly_piece:
                counter += 1
                continue

            else:
                new_y_index = coord[5] + 2
                for num in range(counter):
                    if self._current_board[new_y_index][coord[3]] == ".":
                        return False
                    else:
                        new_y_index += 1
                        continue

                new_y_index = coord[5] + 2
                for num in range(counter):
                    if self._current_board[new_y_index][coord[3]] == enemy_piece:
                        self.set_num_captured_pieces(enemy_piece)
                        self._current_board[new_y_index][coord[3]] = "."
                        new_y_index += 1
                        continue
                break

    def scan_corners(self, old_coord, new_coord):
        """
        Takes old and new coordinates as parameters.  After a piece is moved to one of the eight squares that can
        capture a piece in the nearest corner, it scans various conditions to check if the move constitutes a
        capture.  If so, it updates the number of captured pieces and removes the captured corner piece.
        """

        enemy_piece_color = self.get_enemy_piece_color()
        enemy_piece = self.get_enemy_player()

        if new_coord == "h1" or new_coord == "i2":
            if self.get_square_occupant("h1") == self.get_square_occupant("i2"):
                if self.get_square_occupant("i1") == enemy_piece:
                    self.set_num_captured_pieces(enemy_piece_color)
                    self.set_square_occupant("i1", ".")
                    return True
                else:
                    return False
            else:
                return False

        elif new_coord == "i8" or new_coord == "h9":
            if self.get_square_occupant("i8") == self.get_square_occupant("h9"):
                if self.get_square_occupant("i9") == enemy_piece:
                    self.set_num_captured_pieces(enemy_piece_color)
                    self.set_square_occupant("i9", ".")
                    return True
                else:
                    return False
            else:
                return False

        elif new_coord == "a8" or new_coord == "b9":
            if self.get_square_occupant("a8") == self.get_square_occupant("b9"):
                if self.get_square_occupant("a9") == enemy_piece:
                    self.set_num_captured_pieces(enemy_piece_color)
                    self.set_square_occupant("a9", ".")
                    return True
                else:
                    return False
            else:
                return False

        elif new_coord == "a2" or new_coord == "b1":
            if self.get_square_occupant("a2") == self.get_square_occupant("b1"):
                if self.get_square_occupant("a1") == enemy_piece:
                    self.set_num_captured_pieces(enemy_piece_color)
                    self.set_square_occupant("a1", ".")
                    return True
                else:
                    return False
            else:
                return False

    def is_valid(self, old_coord, new_coord):
        """
        Takes the old and new coordinates as two parameters.  The method will check the proposed move against 
        various conditions and return True if it is a valid move.  Otherwise, it will return False.
        """

        # no skipping turns allowed
        if self.is_skipping_turn(old_coord, new_coord) is True:
            return False

        # if the piece is trying to move from or to a location outside of the board.
        elif self.is_outside_board(old_coord, new_coord) is True:
            return False

        # if moving from an empty square
        elif self.get_square_occupant(old_coord) == "NONE":
            return False

        # if it is a wrong player’s turn.
        elif self.is_wrong_turn(old_coord) is True:
            return False

        # no diagonal moves allowed
        elif self.is_diagonal_move(old_coord, new_coord) is True:
            return False

        # if there is already a piece in the new location
        elif self.get_square_occupant(new_coord) != "NONE":
            return False

        # if the game is already won
        elif self.is_won() is True:
            return False

        # if the piece is trying to jump another piece.
        elif self.is_jumping(old_coord, new_coord) is True:
            return False

        else:
            return True

    def make_move(self, old_coord, new_coord):
        """
        Takes the old and new coordinates on the board as parameters.  If the move is not legal, it will return
        False.  Otherwise, it will call self.is_captured() to see if there are any pieces to be caught.  It will
        then update the board, switch the turn and return True.
        """

        if self.is_valid(old_coord, new_coord) is False:
            print(self._invalid_message)
            return False

        elif self.get_active_player() == "BLUE":
            self.set_square_occupant(old_coord, ".")
            self.set_square_occupant(new_coord, "B")
            self.is_captured(old_coord, new_coord)
            self.switch_active_player()
            self.is_won()
            return True

        elif self.get_active_player() == "ORANGE":
            self.set_square_occupant(old_coord, ".")
            self.set_square_occupant(new_coord, "O")
            self.is_captured(old_coord, new_coord)
            self.switch_active_player()
            self.is_won()
            return True

        else:
            return self._invalid_message

    def play(self, old_coord, new_coord):
        """ 
        Takes the old and new coordinates on the board as parameters.  As the move is validated/made, it shows the
        user the current state of the board and the game including number of captured pieces for each color. 
        """

        make_move_result = self.make_move(old_coord, new_coord)
        blue_captured = self.get_num_captured_pieces("BLUE")
        orange_captured = self.get_num_captured_pieces("ORANGE")

        if self.is_won() is True:
            if self.get_game_state() == "BLUE_WON":
                self.print_board()
                print(f"\n{orange_captured} Orange Pieces Have Been Captured." )
                print("Blue Won.  Goodbye!\n")
            else:
                self.print_board()
                print(f"\n{blue_captured} Blue Pieces Have Been Captured.")
                print("Orange Won.  Goodbye!\n")
                
        else:
            if make_move_result is True:
                #self.make_move(old_coord, new_coord)
                self.print_board()
                print(f"\n{blue_captured} Blue Pieces Have Been Captured.")
                print(f"{orange_captured} Orange Pieces Have Been Captured.\n" )

