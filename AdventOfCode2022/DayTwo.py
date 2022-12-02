class DayTwo:

    def __init__(self, input_path):
        self.input_path = input_path


    def rock_paper_scissors(self, opponent_move, player_move):
        
        points = 0

        if (opponent_move == 'A'):
            if (player_move == 'A' or player_move == 'X'):
                # opponent rock vs player rock = tie
                points = 3
            elif (player_move == 'B' or player_move == 'Y'):
                # opponent rock vs player paper = player wins
                points = 6
            elif (player_move == 'C' or player_move == 'Z'):
                # opponent rock vs player scissors = player loses
                points = 0

        elif (opponent_move == 'B'):
            if (player_move == 'A' or player_move == 'X'):
                # opponent paper vs player rock = player loses
                points = 0
            elif (player_move == 'B' or player_move == 'Y'):
                # opponent paper vs player paper = tie
                points = 3
            elif (player_move == 'C' or player_move == 'Z'):
                # opponent paper vs player scissors = player wins
                points = 6

        elif (opponent_move == 'C'):
            if (player_move == 'A' or player_move == 'X'):
                # opponent scissors vs player rock = player wins
                points = 6
            elif (player_move == 'B' or player_move == 'Y'):
                # opponent scissors vs player paper = player loses
                points = 0
            elif (player_move == 'C' or player_move == 'Z'):
                # opponent scissors vs player scissors = tie
                points = 3

        return points


    def get_player_move(self, opponent_move, required_result):

        player_move = ''

        if (opponent_move == 'A'):
            if (required_result == 'X'):
                # opponent rock vs player scissors = player loses
                player_move = 'C'
            elif (required_result == 'Y'):
                # opponent rock vs player rock = tie
                player_move = 'A'
            elif (required_result == 'Z'):
                # opponent rock vs player paper = player wins
                player_move = 'B'

        elif (opponent_move == 'B'):
            if (required_result == 'X'):
                # opponent paper vs player rock = player loses
                player_move = 'A'
            elif (required_result == 'Y'):
                # opponent paper vs player paper = tie
                player_move = 'B'
            elif (required_result == 'Z'):
                # opponent paper vs player scissors = player wins
                player_move = 'C'

        elif (opponent_move == 'C'):
            if (required_result == 'X'):
                # opponent scissors vs player paper = player loses
                player_move = 'B'
            elif (required_result == 'Y'):
                # opponent scissors vs player scissors = tie
                player_move = 'C'
            elif (required_result == 'Z'):
                # opponent scissors vs player rock = player wins
                player_move = 'A'

        return player_move


    def get_game_score(self, opponent_move, player_move):

        game_score = 0

        if(player_move == 'A' or player_move == 'X'):
            game_score += 1
        elif(player_move == 'B' or player_move == 'Y'):
            game_score += 2
        elif(player_move == 'C' or player_move == 'Z'):
            game_score += 3

        game_score += self.rock_paper_scissors(opponent_move, player_move)

        return game_score


    def part_one(self):

        f = open(self.input_path, "r")
        total_score = 0

        for line in f:
            opponent_move = line[0]
            player_move = line[2]

            total_score += self.get_game_score(opponent_move, player_move)

        return total_score


    def part_two(self):

        f = open(self.input_path, "r")
        total_score = 0
        game_number = 1

        for line in f:
            opponent_move = line[0]
            required_result = line[2]

            player_move = self.get_player_move(opponent_move, required_result)

            total_score += self.get_game_score(opponent_move, player_move)

            game_number += 1

        return total_score
            


day_two = DayTwo("Input/DayTwoInput.txt")

print("Part One Score: " + str(day_two.part_one()))

print("Part Two Score: " + str(day_two.part_two()))