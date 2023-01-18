# write your code here
import random
import itertools
def get_game_list(string):
    global game_list
    game_list = [char if char != "_" else " " for char in string]


def verify_game_string(string):
    test = True
    if len(string) != 9:
        test = False
    for char in string:
        if char not in ["X", "O", "_"]:
            test = False
    return test

def substitute_underscore_space(string):
    for i in range(len(string)):
        if string[i] == "_":
            string[i] = " "
    return string


def print_game_table():
        print("---------")
        print(f"| {game_list[0]} {game_list[1]} {game_list[2]} |")
        print(f"| {game_list[3]} {game_list[4]} {game_list[5]} |")
        print(f"| {game_list[6]} {game_list[7]} {game_list[8]} |")
        print("---------")

def move_X_OR_O():
    x_count = 0
    o_count = 0
    for char in game_list:
        if char == "X":
            x_count += 1
        elif char == "O":
            o_count += 1
    if x_count == o_count:
        return "X"
    else:
        return "O"

def get_game_matrix(game_list):
    A = [0]*3, [0]*3, [0]*3
    g_counter = 0
    for i in range(3):
        for j in range(3):
            A[i][j] = game_list[g_counter]
            g_counter += 1
    return A

def check_occupied(coordinates):
    row = int(coordinates[0])-1
    collumn = int(coordinates[1])-1
    game_matrix = get_game_matrix(game_list)
    if game_matrix[row][collumn] == " ":
        return False
    else:
        return True

def convert_index_to_coordinates(index):
    if index == 0:
        row = 0
        collumn = 0
    elif index == 1:
        row = 0
        collumn = 1
    elif index == 2:
        row = 0
        collumn = 2
    elif index == 3:
        row = 1
        collumn = 0
    elif index == 4:
        row = 1
        collumn = 1
    elif index == 5:
        row = 1
        collumn = 2
    elif index == 6:
        row = 2
        collumn = 0
    elif index == 7:
        row = 2
        collumn = 1
    elif index == 8:
        row = 2
        collumn = 2

    return(f"{row+1} {collumn+1}")

def verify_move_input(string):
    string = string.replace(" ", "")
    if not string.isdigit():
        return "You should enter numbers!"
    elif not (1 <= int(string[0]) <= 3 and 1 <= int(string[1]) <= 3):
        return "Coordinates should be from 1 to 3!"
    else:
        if check_occupied(string) == True:
            return "This cell is occupied! Choose another one!"
        else:
            return None


def convert_move_input_to_index(string):
    string = string.replace(" ", "")
    if string[0]=="1":
        index = 0 + int(string[1]) -1
    elif string[0] == "2":
        index = 3 + int(string[1]) -1
    else:
        index = 6 + int(string[1]) -1
    return index

def check_win_lose_draw():
    winning_sequences = ["012", "345", "678", "036", "147", "258","048", "246"]
    x_win = False
    o_win = False
    game_not_finished = False
    for sequence in winning_sequences:
        seq_count_x = 0
        seq_count_o = 0
        for char in sequence:
            if game_list[int(char)] == "X":
                seq_count_x += 1
            elif game_list[int(char)] == "O":
                seq_count_o += 1
        if seq_count_x == 3 or seq_count_o == 3:
            if seq_count_x == 3:
                x_win = True
                break
            elif seq_count_o == 3:
                o_win = True
                break
    if x_win == False and o_win == False:
        for element in game_list:
            if element == " ":
                game_not_finished = True
                break
    return x_win, o_win, game_not_finished

def start_exit_players(string):
    string_commands = string.split(" ")
    if len(string_commands) == 1:
        if string_commands[0] == "exit":
            return True, None, None, None
        else:
            print("Bad parameters!")
            return False, None, None, None
    else:
        if len(string_commands) < 3:
            print("Bad parameters!")
            return False, None, None, None
        if string_commands[0]!="start":
            print("Bad parameters!")
            return False, None, None, None
        if (string_commands[1]!="easy" and string_commands[1]!="user" and string_commands[1]!="medium" and string_commands[1]!="hard") or (string_commands[2]!="easy" and string_commands[2]!="user" and string_commands[2]!="medium" and string_commands[2]!="hard"):
            print("Bad parameters!")
            return False, None, None, None
        #input commands are mriglin
        return True, string_commands[0], string_commands[1], string_commands[2]

def current_player_alternator(player1, player2):
    while True:
        yield player1
        yield player2

class user:
    def __init__(self):
        pass

    def make_user_move(self):
        present_move = str(input("Enter the coordinates: "))
        while not(verify_move_input(present_move) == None):
            present_move = str(input({verify_move_input(present_move)}))
        present_move = convert_move_input_to_index(present_move)
        X_or_O = "X"
        if X_or_O == "X":
            game_list[present_move] = "X"
        else:
            game_list[present_move] = "O"



class user:
    def __init__(self):
        pass

    def make_user_move(self):
        present_move = str(input("Enter the coordinates: "))
        while not(verify_move_input(present_move) == None):
            present_move = str(input({verify_move_input(present_move)}))
        present_move = convert_move_input_to_index(present_move)
        X_or_O = move_X_OR_O()
        if X_or_O == "X":
            game_list[present_move] = "X"
        else:
            game_list[present_move] = "O"




class easyAI:
    def __init__(self, AI_X_OR_O):
        self.AI_X_OR_O = AI_X_OR_O

    def make_easy_move(self):
        easy_index = int(random.randint(0, 8))
        while not (game_list[easy_index] == " "):
            easy_index = int(random.randint(0, 8))
        X_or_O = move_X_OR_O()
        if X_or_O == "X":
            game_list[easy_index] = "X"
        else:
            game_list[easy_index] = "O"

#independent functions start
def check_one_move_to_win():
        one_move_to_win = False
        sequences = ["01","03","04","12","14","24","25","36","34","45","48","47","46","58","67","78","06","17","28","08","26","02","35","68",]
        x_threat = False
        o_threat = False
        threat_sequence = ""
        for seq in sequences:
            seq_count_x = 0
            seq_count_o = 0
            for char in seq:
                if game_list[int(char)] == "X":
                    seq_count_x += 1
                elif game_list[int(char)] == "O":
                    seq_count_o += 1
            if seq_count_x == 2 or seq_count_o == 2:
                one_move_to_win = True
                threat_sequence = seq
                if seq_count_x == 2:
                    x_threat = True
                    break
                elif seq_count_o == 2:
                    o_threat = True
                    break
        return one_move_to_win, x_threat, o_threat, threat_sequence


#independent functions end

class mediumAI(easyAI):
    def get_winning_move(self, threat_sequence):
        winning_sequences = ["012", "345", "678", "036", "147", "258","048", "246"]
        win_seq = ""
        for seq in winning_sequences:
            count_to_match = 0
            for num_1 in threat_sequence:
                for num_2 in seq:
                    if num_1 == num_2:
                        count_to_match += 1
                        break
            if count_to_match == 2:
                win_seq = seq
                break
        missing_pos = ""

        for num1 in win_seq:
            exist = 0
            for num2 in threat_sequence:
                if num1 == num2:
                    exist = 1
                    break
            if exist == 0:
                missing_pos = num1

        return int(missing_pos)

    def make_medium_move(self):
        one_move_to_win, x_threat, o_threat, threat_sequence= check_one_move_to_win()

        if one_move_to_win == False:
            self.make_easy_move()
        elif one_move_to_win == True:
            X_OR_O = move_X_OR_O()
            winning_move = self.get_winning_move(threat_sequence)
            if X_OR_O == self.AI_X_OR_O:
                if game_list[winning_move] == "X" or game_list[winning_move] == "O":
                    self.make_easy_move()
                else:
                    game_list[winning_move] = X_OR_O
            else:
                pass


class hardAI(mediumAI):
    def move_X_OR_O_minimax(self, current_board):
        x_count = 0
        o_count = 0
        for char in current_board:
            if char == "X":
                x_count += 1
            elif char == "O":
                o_count += 1
        if x_count == o_count:
            return "X"
        else:
            return "O"

    def get_possible_indexes(self, current_board):
        list_of_possibilities = []
        X_OR_O = self.move_X_OR_O_minimax(current_board)
        i = 0
        for pos in current_board:
            if pos == " ":
                list_of_possibilities.append(i)
            i += 1
        return list_of_possibilities

    def check_win_lose_draw_minimax(self, current_board):
        winning_sequences = ["012", "345", "678", "036", "147", "258","048", "246"]
        x_win = False
        o_win = False
        game_not_finished = False
        for sequence in winning_sequences:
            seq_count_x = 0
            seq_count_o = 0
            for char in sequence:
                if current_board[int(char)] == "X":
                    seq_count_x += 1
                elif current_board[int(char)] == "O":
                    seq_count_o += 1
            if seq_count_x == 3 or seq_count_o == 3:
                if seq_count_x == 3:
                    x_win = True
                    break
                elif seq_count_o == 3:
                    o_win = True
                    break
        if x_win == False and o_win == False:
            for element in current_board:
                if element == " ":
                    game_not_finished = True
                    break
        return x_win, o_win, game_not_finished


    def minimax(self, current_board, depth, maxi_p):
        x_win, o_win, game_not_finished = self.check_win_lose_draw_minimax(current_board)
        if (game_not_finished == False):
            if (x_win and self.AI_X_OR_O == "X") or (o_win and self.AI_X_OR_O == "O"):
                return 10, None
            elif game_not_finished == False and x_win == False and o_win == False:
                return 0, None
            else:
                return -10, None


        if maxi_p:
            max_eval = -100000
            best_move = None
            list_of_possibilities = self.get_possible_indexes(current_board)
            for index in list_of_possibilities:
                X_OR_O = self.move_X_OR_O_minimax(current_board)
                current_board[index] = X_OR_O
                evalu, obj = self.minimax(current_board, depth - 1, False)
                if evalu > max_eval:
                    max_eval = evalu
                    best_move = index

                current_board[index] = " "
            return max_eval, best_move
        else:
            min_eval = 100000
            best_move_opponent = None
            list_of_possibilities = self.get_possible_indexes(current_board)
            for index in list_of_possibilities:
                X_OR_O = self.move_X_OR_O_minimax(current_board)
                current_board[index] = X_OR_O
                evalu, obj = self.minimax(current_board, depth - 1, True)
                if evalu < min_eval:
                    min_eval = evalu
                    best_move_opponent = index

                current_board[index] = " "
            return min_eval, best_move_opponent

    def check_empty_game(self):
        empty = True
        for case in game_list:
            if case == "X" or case == "O":
                empty = False
        return empty

    def make_hard_move(self):
        empty = self.check_empty_game()
        if self.AI_X_OR_O == "X" and empty:
            self.make_easy_move()
        else:
            best_score, best_move = self.minimax(game_list, 9, True)
            X_OR_O = move_X_OR_O()
            game_list[best_move] = X_OR_O







def game_loop(player1, player2):

    if (player1 == "easy" or player1 == "medium" or player1 == "hard") and (player2 == "easy" or player2 == "medium" or player2 == "hard"):
        if player1 == "easy" and player2 == "easy":
            AI_1 = easyAI("X")
            def AI_1_move(AI_1): AI_1.make_easy_move()
            print_AI_1 = 'making move level "easy" '
            AI_2 = easyAI("O")
            def AI_2_move(AI_2): AI_2.make_easy_move()
            print_AI_2 = 'making move level "easy" '
        elif player1 == "medium" and player2 == "medium":
            AI_1 = mediumAI("X")
            def AI_1_move(AI_1): AI_1.make_medium_move()
            print_AI_1 = 'making move level "medium" '
            AI_2 = mediumAI("O")
            def AI_2_move(AI_2): AI_2.make_medium_move()
            print_AI_2 = 'making move level "medium" '
        elif player1 == "hard" and player2 == "hard":
            AI_1 = hardAI("X")
            def AI_1_move(AI_1): AI_1.make_hard_move()
            print_AI_1 = 'making move level "hard" '
            AI_2 = hardAI("O")
            def AI_2_move(AI_2): AI_2.make_hard_move()
            print_AI_2 = 'making move level "hard" '
        else:
            if player1 == "medium":
                AI_1 = mediumAI("X")
                def AI_1_move(AI_1): AI_1.make_medium_move()
                print_AI_1 = 'making move level "medium" '
                AI_2 = easyAI("O")
                def AI_2_move(AI_2): AI_2.make_easy_move()
                print_AI_2 = 'making move level "easy" '

            elif player1 == "easy":
                AI_1 = easyAI("X")
                def AI_1_move(AI_1): AI_1.make_easy_move()
                print_AI_1 = 'making move level "easy" '
                AI_2 = mediumAI("O")
                def AI_2_move(AI_2): AI_2.make_medium_move()
                print_AI_2 = 'making move level "medium" '

        print(print_AI_1)
        AI_1_move(AI_1)
        print_game_table()
        x_win, o_win, game_not_finished = check_win_lose_draw()
        while game_not_finished:
            X_OR_O = move_X_OR_O()
            if X_OR_O == "X":
                print(print_AI_1)
                AI_1_move(AI_1)
            elif X_OR_O == "O":
                print(print_AI_2)
                AI_2_move(AI_2)
            print_game_table()
            x_win, o_win, game_not_finished = check_win_lose_draw()
            if x_win:
                print("X wins")
            elif o_win:
                print("O wins")
            elif not game_not_finished and (x_win == False and o_win == False):
                print("Draw")
    else:
        if player1 == "user":
            user_1 = user()
            if player2 == "easy":
                AI = easyAI("O")
                def AI_move(AI): AI.make_easy_move()
                level_move = 'making move level "easy"'
            elif player2 == "medium":
                AI = mediumAI("O")
                def AI_move(AI): AI.make_medium_move()
                level_move = 'making move level "medium"'
            else:
                AI = hardAI("O")
                def AI_move(AI): AI.make_hard_move()
                level_move = 'making move level "hard"'



            X_OR_O = move_X_OR_O()
            user_1.make_user_move()
            print_game_table()
            x_win, o_win, game_not_finished = check_win_lose_draw()
            while game_not_finished:
                X_OR_O = move_X_OR_O()
                if X_OR_O == "X":
                    user_1.make_user_move()
                else:
                    print(level_move)
                    AI_move(AI)

                print_game_table()
                x_win, o_win, game_not_finished = check_win_lose_draw()
                if x_win:
                    print("X wins")
                elif o_win:
                    print("O wins")
                elif not game_not_finished and (x_win == False and o_win == False):
                    print("Draw")
        elif player2 == "user":
            user_2 = user()
            if player1 == "easy":
                AI = easyAI("X")
                def AI_move(AI): AI.make_easy_move()
                level_move = 'making move level "easy"'

            elif player1 == "medium":
                AI = mediumAI("X")
                def AI_move(AI): AI.make_medium_move()
                level_move = 'making move level "medium"'
            else:
                AI = hardAI("X")
                def AI_move(AI): AI.make_hard_move()
                level_move = 'making move level "hard"'



            print(level_move)
            AI_move(AI)
            print_game_table()
            x_win, o_win, game_not_finished = check_win_lose_draw()
            while game_not_finished:
                X_OR_O = move_X_OR_O()
                if X_OR_O == "X":
                    print(level_move)
                    AI_move(AI)
                else:
                    user_2.make_user_move()

                print_game_table()
                x_win, o_win, game_not_finished = check_win_lose_draw()
                if x_win:
                    print("X wins")
                elif o_win:
                    print("O wins")
                elif not game_not_finished and (x_win == False and o_win == False):
                    print("Draw")






def game_start():
    game_string = "_________"
    get_game_list(game_string)
    command_string = str(input("Input command:"))
    pass_ok, start_or_exit, player1, player2 = start_exit_players(command_string)
    while not pass_ok:
        command_string = str(input("Input command:"))
        pass_ok, start_or_exit, player1, player2 = start_exit_players(command_string)
    if start_or_exit == "start":
        print_game_table()
        game_loop(player1, player2)
    else:
        pass



#Main program
game_start()







