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

        # picking mine hand
        if 'X' in line:
            my_hand = 'rock'
            round_score += 1
        elif 'Y' in line:
            my_hand = 'paper'
            round_score += 2
        elif 'Z' in line:
            my_hand = 'scissors'
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