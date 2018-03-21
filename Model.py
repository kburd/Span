import os
from City import *
from Configuration import Configuration


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


class Model:

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
