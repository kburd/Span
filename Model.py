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

        for i in range(len(self.sampleSet)):

            fatherCity = choice(self.sampleSet)
            motherCity = choice(self.sampleSet)

            childCity = City(self.config.citySize)

            for j in range(self.config.citySize):
                for k in range(self.config.citySize):

                    fatherBlock = fatherCity.getBlock(j, k)
                    motherBlock = motherCity.getBlock(j, k)
                    childZone = None

                    if fatherBlock.zoning == motherBlock.zoning:
                        childZone = fatherBlock.zoning

                    else:
                        parent = randint(1, 2)

                        if parent == 1:
                            childZone = fatherBlock.zoning
                        else:
                            childZone = motherBlock.zoning


                    mutationChance = randint(0, 100)

                    if mutationChance < self.config.mutationThreshold:

                        childZone = Zone.RANDOM

                    childCity.setBlock(j, k, childZone)

            newSampleSet += [self.sampleSet[i]]
            newSampleSet += [childCity]

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
