from twisted.internet import protocol, reactor

PORT = 12345
HOST = "localhost"


class TSCliProtocol(protocol.Protocol):

    def sendData(self):
        data = input("cli：")
        if data:
            self.transport.write(data)
        self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data)
        self.sendData()


class TSCliFactory(protocol.ClientFactory):
    protocol = TSCliProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSCliFactory())
reactor.run()
