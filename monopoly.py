from random import randint
import matplotlib.pyplot as plt

def roll():
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    flag = False

    if roll1 == roll2: 
        flag = True

    return [flag, roll1, roll2]  

class Player:
    def __init__(self, id):
        self.id = id
        self.position = 0

    def move(self, moveby):
        if self.position + moveby > 39:
            moveby -= 40 - self.position
            self.position = 0
            self.position += moveby
        else:
            self.position += moveby
        
        if self.position in Board.moves:
            Board.moves[self.position] += 1
        else:
            Board.moves[self.position] = 1

class Tile:
    def __init__(self, name, color, rent):
        self.name = name
        self.color = color
        self.rent = rent

class Board:
    players = list()
    tiles = list()
    moves = {}

    def __init__(self, players, filename):
        Board.makeTiles(self, filename)
        for x in range(players):
            Board.players.append(Player(x))

    def makeTiles(self, filename):
        with open(filename, "r") as f:
            for line in f:
                wordArray = line.split()
                Board.tiles.append(Tile(wordArray[0], wordArray[1], wordArray[2]))
    
    def movePlayer(self, player, moveby):
        self.players[player].move(moveby)

    def rollDie(self):
        for x in range(len(Board.players)):
            moveby = 0
            for i in xrange(3):
                #print("rolling", i)
                rolls = roll()
                #print(rolls)
                moveby += rolls[1] + rolls[2]
                if(rolls[0] == False):
                    break
            if(rolls[0] == True):
                    print("speeding!")
                    if 10 in Board.moves:
                        Board.moves[10] += 1
                    else:
                        Board.moves[10] = 1
            else:
                #print(moveby)
                Board.movePlayer(self, x, moveby)
            

    def printBoard(self):
        for x in range(len(self.tiles)):
            print(self.tiles[x].name)
    
    def printStats(self):
        print(Board.moves)
        for x in range(len(Board.players)):
            print("player#", x, Board.players[x].position)
        
        barplot = plt.bar(range(len(Board.moves)), list(Board.moves.values()))

        labels = []
        for i in range(len(Board.tiles)):
            labels.append(Board.tiles[i].name)
        plt.xticks(range(len(Board.tiles)), labels, rotation='vertical')
        plt.subplots_adjust(bottom=0.4)
        plt.title("rolls results")
        for i in range(len(Board.tiles)):
            barplot[i].set_color(Board.tiles[i].color)
        plt.show()
    
game = Board(1, "init.txt")
for x in range(0, 500):
    game.rollDie()
game.printBoard()
game.printStats()