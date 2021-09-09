import random
import numpy as np

test_cases = int(input())


class Dice:
    def __init__(self, prob):
        self.prob = prob
        self.move = 0
        self.num_prob = [float(n) for n in self.prob.split(",")]
        self.num_prob = np.cumsum(self.num_prob)

    def Roll(self):
        roll = round(random.uniform(0.01, 1), 2)
        if roll <= self.num_prob[0]:
            self.move = 1
        elif self.num_prob[0] < roll <= self.num_prob[1]:
            self.move = 2
        elif self.num_prob[1] < roll <= self.num_prob[2]:
            self.move = 3
        elif self.num_prob[2] < roll <= self.num_prob[3]:
            self.move = 4
        elif self.num_prob[3] < roll <= self.num_prob[4]:
            self.move = 5
        else:
            self.move = 6
        return self.move


class Board:
    def __init__(self, l_move, s_move, position):
        self.board = [n for n in range(0, 101)]
        self.l_move = [n.split(",") for n in l_move.split(" ")]
        self.s_move = [n.split(",") for n in s_move.split(" ")]
        self.l_dict = {}
        self.position = self.board[position]
        self.end_game = False
        for pack in self.l_move:
            self.l_dict[int(pack[0])] = int(pack[1])
        self.s_dict = {}
        for pack in self.s_move:
            self.s_dict[int(pack[0])] = int(pack[1])
        self.board = [self.l_dict.get(n, n) for n in self.board]
        self.board = [self.s_dict.get(n, n) for n in self.board]

    def Win(self):
        self.end_game = True

    def Move(self, move):
        if self.position + move > 100:
            pass
        elif self.position + move == 100:
            self.Win()
        else:
            self.position += move
        self.position = self.board[self.position]


lst = []

for _ in range(test_cases):
    lst1 = []
    prob1 = input()
    ls1 = input()
    l1_move = input()
    s1_move = input()
    for _ in range(5000):
        board = Board(l1_move, s1_move, 1)
        dice = Dice(prob1)
        turn = 0
        while not board.end_game:
            if turn > 1000:
                turn = 1000
                break
            else:
                turn += 1
                board.Move(dice.Roll())
        lst1.append(turn)
    print(np.mean(lst1))

# 171.233
# 95.2886
# 167.4198
