from City import *


class Model:

    def __init__(self):

        self.config = Configuration()
        self.sampleSet = []
        self.generation = 0

    def generate(self):

        self.generation = 1
        self.sampleSet = []

        for n in range(self.config.sampleSize):

            self.sampleSet += [City(self.config.citySize)]

    def analyze(self):

        for city in self.sampleSet:

            city.analyze(self.config)

    def sort(self):

        self.sampleSet.sort()

    def delete(self):

        self.sampleSet = self.sampleSet[self.config.sampleSize//2:]

    def mutate(self):

        newSampleSet = []

        for oldCity in self.sampleSet:

            newCity = City(self.config.citySize)

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

    # def saveSimulation(self):
    #
    #     saveDir = "Simulation"
    #
    #     if not os.path.isdir(saveDir):
    #         os.mkdir(saveDir)
    #
    #     for city in self.sampleSet:
    #
    #         city.save(saveDir)
    #
    # def loadSimulation(self):
    #
    #     for i in range(self.config.sampleSize):
    #
    #         city = City(self.config.citySize, i+1)
    #         city.load()
    #
    #         self.sampleSet += [city]
