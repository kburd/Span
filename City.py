from random import randint, choice
from enum import Enum


class Zone(Enum):

    EMPTY = 0
    RESIDENTIAL = 1
    COMMERCIAL = 2
    INDUSTRIAL = 3
    # AGRICULTURAL = 4
    # HOSPITAL = 5
    # EDUCATIONAL = 6
    # RECREATIONAL = 7
    # ROAD = 8
    RANDOM = 4


class Score:

    def __init__(self):

        self.pollution = 0
        self.commerce = 0
        self.food = 0

    def __add__(self, other):

        newScore = Score()

        newScore.pollution = self.pollution + other.pollution
        newScore.commerce = self.commerce + other.commerce
        newScore.food = self.food + other.food

        return newScore


class Block:

    def __init__(self):

        self.zoning = None
        self.score = Score()

    # def show(self):
    #     raise NotImplementedError


class Empty(Block):

    def __init__(self):

        super().__init__()
        self.zoning = Zone.EMPTY

    def show(self):

        return None


class Industrial:

    def __init__(self):

        self.zoning = Zone.INDUSTRIAL


class Residential:

    def __init__(self):

        self.zoning = Zone.RESIDENTIAL


class Commercial:

    def __init__(self):

        self.zoning = Zone.COMMERCIAL


class City:

    def __init__(self, size):

        self.layout = []
        self.size = size
        self.rating = 0

        for i in range(size):

            row = []

            for j in range(size):

                row += [None]

            self.layout += [row]

        for i in range(len(self.layout)):
            for j in range(len(self.layout[i])):
                self.setBlock(i, j, Zone.RANDOM)

    def __str__(self):

        string = ""

        for row in self.layout:
            for block in row:
                string += str(block.zoning.value)
            string += "\n"

        return string

    def __lt__(self, other):

        return self.rating < other.rating

    def getBlock(self, row, col):

        return self.layout[row][col]

    def setBlock(self, row, col, zone):

        if zone == Zone.RANDOM:

            zone = Zone(randint(0, Zone.RANDOM.value - 1))

        if zone == Zone.EMPTY:

            self.layout[row][col] = Empty()

        elif zone == Zone.INDUSTRIAL:

            self.layout[row][col] = Industrial()

        elif zone == Zone.COMMERCIAL:

            self.layout[row][col] = Commercial()

        elif zone == Zone.RESIDENTIAL:

            self.layout[row][col] = Residential()

    def getSurrondingBlocks(self, row, col, distance):

        neighborhood = []

        for m in range(-distance, distance + 1):
            for n in range(-distance, distance + 1):

                if row + m >= 0 and row + m < self.size and col + n >= 0 and col + n < self.size \
                        and not (m == 0 and n == 0):

                    neighborhood += [self.getBlock(row + m, col + n)]

        return neighborhood

    def analyze(self, config):

        score = 0

        for i in range(self.size):
            for j in range(self.size):

                blockZone = self.getBlock(i, j).zoning
                blockScore = 0
                scoreRemoval = False

                if blockZone == Zone.RESIDENTIAL:

                    neighborhood = self.getSurrondingBlocks(i, j, config.walkingDistance)

                    for neighbor in neighborhood:

                        if neighbor.zoning == Zone.COMMERCIAL:
                            blockScore += 1

                    neighborhood = self.getSurrondingBlocks(i, j, 1)

                    for neighbor in neighborhood:

                        if neighbor.zoning == Zone.INDUSTRIAL:
                            scoreRemoval = True



                # elif blockZone == Zone.COMMERCIAL:
                #
                #     neighborhood = self.getSurrondingBlocks(i, j, simulator.walkingDistance)
                #
                #     for neighbor in neighborhood:
                #
                #         if neighbor.zoning == Zone.COMMERCIAL:
                #             blockScore -= 1

                elif blockZone == Zone.INDUSTRIAL:

                    if i == 0 or j == 0 or i == self.size - 1 or j == self.size - 1:
                        blockScore = 10

                    else:
                        scoreRemoval = True

                if scoreRemoval:
                    blockScore = 0

                score += blockScore

        self.rating = score

    # def save(self, dir):
    #
    #     string = ""
    #
    #     for row in self.layout:
    #
    #         for block in row:
    #
    #             string += str(block.zoning.value) + ","
    #
    #         string += "\n"
    #
    #     open(dir + "\\" + self.id + ".txt", "w").write(string)
    #
    # def load(self):
    #
    #     rawText = open(self.id + ".txt", 'r').readlines()
    #
    #     for i in range(len(rawText)):
    #
    #         row = rawText[i].strip(",\n").split(",")
    #
    #         for j in range(len(row)):
    #
    #             self.layout[i][j] = Block(Zone(int(row[j])))


class Configuration:

    def __init__(self):

        configFile = open("config.txt", 'r')
        rawData = configFile.readlines()

        data = []
        for line in rawData:

            if line[0] != "#" and line[0] != "\n":
                data += [line.strip("\n")]

        self.sampleSize = int(data[0])
        self.citySize = int(data[1])
        self.mutationThreshold = int(data[2])

        self.walkingDistance = int(data[3])

        numOfZones = Zone.RANDOM.value
        self.colors = []
        for i in range(numOfZones):
            self.colors += [data[4 + i]]
