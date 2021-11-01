import random


def play():
    user = input("Choose 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You win!'
    if is_win(computer, user):
        return 'You lost!'


def is_win(player, opponent):
    # return true if player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
