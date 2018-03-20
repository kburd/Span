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
