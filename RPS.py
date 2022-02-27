import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass

    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def valid_input(self):
        while True:
            move = input("Rock, Paper, Scissors? > ").lower()
            if move in moves:
                return move
            else:
                print("I don't understand. Please try again.")

    def move(self):
        return self.valid_input()


class ReflectPlayer(Player):

    def __init__(self):
        self.my_next_move = None

    # change instance variable to "learn" what was played
    def learn(self, my_move, their_move):
        self.my_next_move = their_move

    def move(self):
        # needs if statement, since the first "move" method call
        # in the "play-round" function occurs
        # before anything is "learned"
        if self.my_next_move is not None:
            return self.my_next_move
        else:
            return random.choice(moves)


class CyclePlayer(Player):

    def __init__(self):
        self.my_move = None
        self.index = 0

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is not None:
            # find the index of the out of "moves" randomly chosen
            # item called "move"
            self.index = moves.index(self.my_move)
            # circle through list "moves"
            self.index = (self.index + 1) % len(moves)
            move = moves[self.index]
            return move
        else:
            # first choice is random
            return random.choice(moves)


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_player1 = 0
        self.score_player2 = 0

    # refactored score announcement
    def print_score(self):
        print("Score: "
              f"Player One: {self.score_player1}, "
              f"Player Two: {self.score_player2}")

    def keep_score(self, one, two):
        if HumanPlayer.beats(one, two):
            self.score_player1 += 1
            self.print_score()

        elif one == two:
            print("*** TIE ***")
            self.print_score()
        else:
            self.score_player2 += 1
            self.print_score()

    def play_round(self):
        # local variable to store object's method call's, ('move'),
        # returned value and pass it as an arg. to the other methods
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.keep_score(move1, move2)

    def play_game(self):
        print("The player who has 3 points more "
              "than the opponent does wins the game!\n"
              "Game start!")
        round = 0

        # play until one player is up by 3 points
        while abs(self.score_player1
                  - self.score_player2) != 3:
            round += 1
            print(f"Round {round}:")
            self.play_round()
        self.final_score_announcement()

    def final_score_announcement(self):
        if self.score_player1 > self.score_player2:
            print("\n****-Player 1 wins!!!-****\n"
                  "Final Score: "
                  f"Player One: {self.score_player1} "
                  f"Player Two: {self.score_player2} \n"
                  )
        else:
            print("\n****-Player 2 wins!!!-****\n"
                  "Final Score: "
                  f"Player One: {self.score_player1} "
                  f"Player Two: {self.score_player2} \n"
                  )


if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']
    game = Game(HumanPlayer(), Player())
    game.play_game()
