from Zones import Zone
from random import randint


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