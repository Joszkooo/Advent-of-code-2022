total_score: int = 0
round_score: int
my_hand: str
opponent_hand: str


with open('input.txt', 'r') as file:
    line = file.readline()
    while line:
        round_score = 0

        # picking opponent hand
        if 'A' in line:
            opponent_hand = 'rock'
        elif 'B' in line:
            opponent_hand = 'paper'
        elif 'C' in line:
            opponent_hand = 'scissors'

        # picking result of round
        if 'X' in line:
            result = 'lose'
        elif 'Y' in line:
            result = 'draw'
        elif 'Z' in line:
            result = 'win'

        # picking my hand
        if result == 'draw':
            my_hand = opponent_hand
        elif result == 'lose':
            if opponent_hand == 'rock':
                my_hand = 'scissors'
            elif opponent_hand == 'paper':
                my_hand = 'rock'
            elif opponent_hand == 'scissors':
                my_hand = 'paper'
        elif result == 'win':
            if opponent_hand == 'rock':
                my_hand = 'paper'
            elif opponent_hand == 'paper':
                my_hand = 'scissors'
            elif opponent_hand == 'scissors':
                my_hand = 'rock'

        # adding points for shape

        if my_hand == 'rock':
            round_score += 1

        elif my_hand == 'paper':
            round_score += 2

        if my_hand == 'scissors':
            round_score += 3

        # checking round
        if my_hand == opponent_hand:
            round_score += 3

        elif my_hand == "rock":
            if opponent_hand == "scissors":
                round_score += 6
            else:
                round_score += 0

        elif my_hand == "paper":
            if opponent_hand == "rock":
                round_score += 6
            else:
                round_score += 0

        elif my_hand == "scissors":
            if opponent_hand == "paper":
                round_score += 6
            else:
                round_score += 0

        total_score += round_score
        line = file.readline()

print(total_score)
