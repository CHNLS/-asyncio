from twisted.internet import protocol, reactor
from time import ctime

PORT = 12345  # 定义一个常量端口


class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        client = self.client = self.transport.getPeer().host
        print(self.client)
        print("连接自：", client)

    def dataReceived(self, data):
        self.transport.write("[%s] %s" % (ctime(), data))


factory = protocol.Factory()
factory.protocol = TSServerProtocol
print("等待连接...")
reactor.listenTCP(PORT, factory)
reactor.run()



