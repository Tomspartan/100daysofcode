import random


class Player:
    def __init__(self, name):
        self.name = name


class Roll:
    def __init__(self, name, can_defeat, defeated_by):
        self.name = name
        self.can_defeat = can_defeat
        self.defeated_by = defeated_by


def main():
    print_header()
    rolls = build_the_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Professor Buttstuff")

    game_loop(player1, player2, rolls)


def print_header():
    print('-------------')
    print('Rock Paper Scissors Game')
    print('-------------')


def build_the_rolls():
    rolls = {
        'Rock': Roll('Rock', 'Scissors', 'Paper'),
        'Scissors': Roll('Scissors', 'Paper', 'Rock'),
        'Paper': Roll('Paper', 'Rock', 'Scissors')
        }
    return rolls


def get_players_name():
    name = input('Please enter your name ')
    return name


def game_loop(player1, player2, rolls):
    count = 0
    while count < 3:
        p2_roll = random.choice(list(rolls.values()))
        p1_input = input('What do you throw? [r]ock, [p]aper or [s]cissors? ')
        if p1_input == 'r':
            p1_roll = rolls['Rock']
        elif p1_input == 'p':
            p1_roll = rolls['Paper']
        elif p1_input == 's':
            p1_roll = rolls['Scissors']
        print(player2.name+" rolls a "+p2_roll.name)
        if p1_roll == p2_roll:
            print('Round is a tie, try again')
            count -= 1
        elif p1_roll.name == p2_roll.defeated_by:
            print(player1.name+" wins")
        elif p2_roll.name == p1_roll.defeated_by:
            print(player2.name+" wins")
        count += 1


if __name__ == '__main__':
    main()