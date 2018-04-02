from Model import *


def autoRun(saveLocation):

    file = open(saveLocation, "a")

    model = Model()

    model.generate()
    model.analyze()
    model.sort()

    while 1000 >= model.generation:

        model.delete()
        model.mutate()
        model.analyze()
        model.sort()
        model.generation += 1

    file.write(str(model.sampleSet[-1].rating) + "\n")
    file.close()

    return model.sampleSet[-1].rating


filename = "Test\\gradientResults.txt"

for i in range(10):
    result = autoRun(filename)
    print(i+1, result, sep=": ")


file = open(filename)
lines = file.read().split("\n")
del lines[-1]

total = 0

for line in lines:

    total += int(line)

print(round(total/len(lines)))


