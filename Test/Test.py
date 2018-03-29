from Model import *


def autoRun(maxRating, saveLocation):

    file = open(saveLocation, "a")

    model = Model()

    model.generate()
    model.analyze()
    model.sort()

    while model.sampleSet[-1].rating != maxRating:

        model.delete()
        model.mutate()
        model.analyze()
        model.sort()
        model.generation += 1

    file.write(str(model.generation) + "\n")
    file.close()

    return model.generation


# for i in range(10):
#     result = autoRun(492, "testResults.txt")
#     print(i+1, result, sep=": ")


file = open("testResults.txt")
lines = file.read().split("\n")
del lines[-1]

total = 0

for line in lines:

    total += int(line)

print(round(total/len(lines)))


