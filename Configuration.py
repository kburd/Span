from Zones import Zone


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