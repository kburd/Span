from http.server import BaseHTTPRequestHandler, HTTPServer
from Model import Zone

class View:

    def createGUI(self, simulator):

        message = ""
        lines = open("HTML\\resource.html", "r").readlines()

        if simulator.sampleSet == []:

            gen = "-"
            worst = "-"
            median = "-"
            best = "-"
            cityHTML = "<canvas id='myCanvas' width='500' height='500' style='background-color:LightGray;'>Test</canvas>"

        else:

            city = simulator.sampleSet[-1]

            gen = str(simulator.generation)
            worst = str(simulator.sampleSet[0].rating)
            median = str(simulator.sampleSet[len(simulator.sampleSet) // 2].rating)
            best = str(simulator.sampleSet[-1].rating)

            cityHTML = ""
            blockLength = str((500 - simulator.config.citySize) // city.size)
            for row in city.layout:
                cityHTML += "<tr>"
                for block in row:
                    cityHTML += "<td>"
                    cityHTML += "<canvas width=" + blockLength + " height=" + blockLength + \
                                " style='background-color:" + simulator.config.colors[
                                    block.zoning.value] + "';>Test</canvas>"
                    cityHTML += "</td>"
                cityHTML += "</tr>"

        legend = ""
        for i in range(Zone.RANDOM.value):
            legend += "<tr>"
            legend += "<td><canvas id='myCanvas' width='15' height='15' style='background-color:" + \
                      simulator.config.colors[i] + ";'>Test</canvas></td>"
            legend += "<td>" + str(Zone(i).name) + "</td>"
            legend += "</tr>"

        for line in lines:
            temp = line.strip()
            if temp == "*city*":
                message += cityHTML
            elif temp == "*generation*":
                message += gen
            elif temp == "*worst*":
                message += worst
            elif temp == "*median*":
                message += median
            elif temp == "*best*":
                message += best
            elif temp == "*legend*":
                message += legend
            else:
                message += line

        return message