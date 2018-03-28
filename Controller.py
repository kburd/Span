from http.server import BaseHTTPRequestHandler, HTTPServer
from Model import *
from View import *

model = None
view = View()

def getValue(key, requestString):

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


class RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        global model
        global view

        mode = getValue("mode", self.requestline)
        message = format("%s is not a mode") % mode

        if mode == "echo":
            message = "Hola Mundo"

        if mode == 'init':
            message = view.createGUI(model)

        if mode == "newSim":

            model = Model()
            view = View()

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
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


def run():

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running Span...')
    httpd.serve_forever()


run()
