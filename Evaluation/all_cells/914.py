# starten van de webserver :)
apps = {'/': Application(FunctionHandler(make_document))}

server = Server(apps, port=5006, allow_websocket_origin=['localhost:5006','nm-interactive.net:5006'])
server.start()