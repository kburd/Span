from http.server import BaseHTTPRequestHandler, HTTPServer
from Model import *
from View import *

requestString = ''
model = Model()
view = View()

def getValue(key):

    paramString = requestString.split(" ")[1].strip("/")
    pairs = paramString.split("&")

    for i in range(len(pairs)):
        pair = pairs[i].split("=")

        if len(pair) == 1:
            return

        tempKey = pair[0]
        tempValue = pair[1]

        if tempKey == key:

            return tempValue


# def createGUI(city):
#
#     message = ""
#     lines = open("HTML\\resource.html", "r").readlines()
#
#     if city == None:
#
#         gen = "-"
#         worst = "-"
#         median = "-"
#         best = "-"
#         cityHTML = "<canvas id='myCanvas' width='500' height='500' style='background-color:LightGray;'>Test</canvas>"
#
#     else:
#         gen = str(simulator.generation)
#         worst = str(simulator.sampleSet[0].rating)
#         median = str(simulator.sampleSet[len(simulator.sampleSet)//2].rating)
#         best = str(simulator.sampleSet[-1].rating)
#
#         cityHTML = ""
#         blockLength = str((500-simulator.config.citySize)//city.size)
#         for row in city.layout:
#             cityHTML += "<tr>"
#             for block in row:
#                 cityHTML += "<td>"
#                 cityHTML += "<canvas width=" + blockLength + " height=" + blockLength +\
#                           " style='background-color:" + simulator.config.colors[block.zoning.value] + "';>Test</canvas>"
#                 cityHTML += "</td>"
#             cityHTML += "</tr>"
#
#
#
#     legend = ""
#     for i in range(Zone.RANDOM.value):
#         legend += "<tr>"
#         legend += "<td><canvas id='myCanvas' width='15' height='15' style='background-color:" + \
#                   simulator.config.colors[i] + ";'>Test</canvas></td>"
#         legend += "<td>" + str(Zone(i).name) + "</td>"
#         legend += "</tr>"
#
#     for line in lines:
#         temp = line.strip()
#         if temp == "*city*":
#             message += cityHTML
#         elif temp == "*generation*":
#             message += gen
#         elif temp == "*worst*":
#             message += worst
#         elif temp == "*median*":
#             message += median
#         elif temp == "*best*":
#             message += best
#         elif temp == "*legend*":
#             message += legend
#         else:
#             message += line
#
#     return message


# HTTPRequestHandler class


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        global requestString
        global model
        requestString = self.requestline

        mode = getValue("mode")
        message = format("%s is not a mode") % mode

        if mode == "echo":
            message = "Hola Mundo"

        if mode == 'init':
            message = view.createGUI(model)

        if mode == "newSim":

            model = Model()
            model.generate()
            model.analyze()
            model.sort()
            message = view.createGUI(model)

        if mode == "oneGen":
            model.delete()
            model.mutate()
            model.analyze()
            model.sort()
            model.generation += 1
            message = view.createGUI(model)

        if mode == "tenGen":
            for i in range(10):
                model.delete()
                model.mutate()
                model.analyze()
                model.sort()
                model.generation += 1
            message = view.createGUI(model)

        if mode == "hundredGen":
            for i in range(100):
                model.delete()
                model.mutate()
                model.analyze()
                model.sort()
                model.generation += 1
            message = view.createGUI(model)

        if mode == "thousandGen":
            for i in range(1000):
                model.delete()
                model.mutate()
                model.analyze()
                model.sort()
                model.generation += 1
            message = view.createGUI(model)

        # if mode == "viewWorst":
        #     message = view.createGUI(model)
        #
        # if mode == "viewMedian":
        #     message = view.createGUI(model.sampleSet[len(model.sampleSet) // 2])
        #
        # if mode == "viewBest":
        #     message = view.createGUI(model.sampleSet[-1])

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        self.send_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


def run():

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('Running Span...')
    httpd.serve_forever()


run()