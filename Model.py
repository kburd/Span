import os
from City import *
from enum import Enum
from random import randint

# class Zone(Enum):
#     EMPTY = 0
#     RESIDENTIAL = 1
#     COMMERCIAL = 2
#     INDUSTRIAL = 3
#     AGRICULTURAL = 4
#     HOSPITAL = 5
#     EDUCATIONAL = 6
#     RECREATIONAL = 7
#     ROAD = 8
#     RANDOM = 9
#
#
# class Block:
#
#     def __init__(self, zoning):
#
#         self.zoning = zoning
#
#         if self.zoning == Zone.RANDOM:
#             num = randint(0, Zone.RANDOM.value-1)
#             self.zoning = Zone(num)
#
#
# class City:
#
#     def __init__(self, size, id):
#
#         self.layout = []
#         self.size = size
#         self.rating = 0
#         self.id = str(id)
#
#         for i in range(size):
#
#             row = []
#
#             for j in range(size):
#
#                 row += [Block(Zone.RANDOM)]
#
#             self.layout += [row]
#
#     def __str__(self):
#
#         string = ""
#
#         for row in self.layout:
#             for block in row:
#                 string += str(block.zoning.value)
#             string += "\n"
#
#         return string
#
#     def __lt__(self, other):
#
#         return self.rating < other.rating
#
#     def getBlock(self, row, col):
#
#         return self.layout[row][col]
#
#     def setBlock(self, row, col, block):
#
#         self.layout[row][col] = block
#
#     def getSurrondingBlocks(self, row, col, distance):
#
#         neighborhood = []
#
#         for m in range(-distance, distance + 1):
#             for n in range(-distance, distance + 1):
#
#                 if row + m >= 0 and row + m < self.size and col + n >= 0 and col + n < self.size \
#                         and not (m == 0 and n == 0):
#
#                     neighborhood += [self.getBlock(row + m, col + n)]
#
#         return neighborhood
#
#     def save(self, dir):
#
#         string = ""
#
#         for row in self.layout:
#
#             for block in row:
#
#                 string += str(block.zoning.value) + ","
#
#             string += "\n"
#
#         open(dir + "\\" + self.id + ".txt", "w").write(string)
#
#     def load(self):
#
#         rawText = open(self.id + ".txt", 'r').readlines()
#
#         for i in range(len(rawText)):
#
#             row = rawText[i].strip(",\n").split(",")
#
#             for j in range(len(row)):
#
#                 self.layout[i][j] = Block(Zone(int(row[j])))


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


class Block:

    def __init__(self):

        self.zoning = None

    def show(self):
        raise NotImplementedError


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

    def __init__(self, size, id):

        self.layout = []
        self.size = size
        self.rating = 0
        self.id = str(id)

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

    def save(self, dir):

        string = ""

        for row in self.layout:

            for block in row:

                string += str(block.zoning.value) + ","

            string += "\n"

        open(dir + "\\" + self.id + ".txt", "w").write(string)

    def load(self):

        rawText = open(self.id + ".txt", 'r').readlines()

        for i in range(len(rawText)):

            row = rawText[i].strip(",\n").split(",")

            for j in range(len(row)):

                self.layout[i][j] = Block(Zone(int(row[j])))


class Analyzer:

    def __init__(self, config):

        self.config = config

        self.foodScore = 0
        self.pollutionScore = 0
        self.economicScore = 0


    def analyze(self, city):

        score = 0

        for i in range(city.size):
            for j in range(city.size):

                blockZone = city.getBlock(i, j).zoning
                blockScore = 0
                scoreRemoval = False

                if blockZone == Zone.RESIDENTIAL:

                    neighborhood = city.getSurrondingBlocks(i, j, self.config.walkingDistance)

                    for neighbor in neighborhood:

                        if neighbor.zoning == Zone.COMMERCIAL:
                            blockScore += 1

                    neighborhood = city.getSurrondingBlocks(i, j, 1)

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

                    if i == 0 or j == 0 or i == city.size - 1 or j == city.size - 1:
                        blockScore = 10

                    else:
                        scoreRemoval = True

                if scoreRemoval:
                    blockScore = 0

                score += blockScore

        city.rating = score


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


class Simulation:

    def __init__(self):

        self.config = Configuration()
        self.analyzer = Analyzer(self.config)
        self.sampleSet = []
        self.generation = 0

    def generate(self):

        id = 1
        self.generation = 1
        self.sampleSet = []

        for n in range(self.config.sampleSize):

            self.sampleSet += [City(self.config.citySize, id)]
            id += 1

    def analyze(self):

        for city in self.sampleSet:

            self.analyzer.analyze(city)
            #city.analyzeExample()

    def sort(self):

        self.sampleSet.sort()

    def delete(self):

        self.sampleSet = self.sampleSet[self.config.sampleSize//2:]

    def mutate(self):

        newSampleSet = []

        for oldCity in self.sampleSet:

            newCity = City(self.config.citySize, oldCity.id)

            for i in range(self.config.citySize):
                for j in range(self.config.citySize):

                    oldBlock = oldCity.getBlock(i, j)

                    chance = randint(0, 100)

                    if chance < self.config.mutationThreshold:

                        newCity.setBlock(i, j, Zone.RANDOM)

                    else:

                        newCity.setBlock(i, j, oldBlock.zoning)

            newSampleSet += [oldCity]
            newSampleSet += [newCity]

        self.sampleSet = newSampleSet

    def saveSimulation(self):

        saveDir = "Simulation"

        if not os.path.isdir(saveDir):
            os.mkdir(saveDir)

        for city in self.sampleSet:

            city.save(saveDir)

    def loadSimulation(self):

        for i in range(self.config.sampleSize):

            city = City(self.config.citySize, i+1)
            city.load()

            self.sampleSet += [city]
