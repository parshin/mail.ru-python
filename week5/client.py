import socket
import time


class Client:
    def __init__(self, server_address, server_port, timeout=None):
        self.server_address = server_address
        self.server_port = server_port
        self.timeout = timeout

    def read_data(self, sock):
        # while '\n\n' not in data:
        data = sock.recv(4096)
        return data

    def put(self, metric, value, timestamp=time.time()):
        with socket.create_connection((self.server_address, self.server_port), self.timeout) as sock:
            try:
                msg = 'put {} {} {}\n'.format(metric, value, str(int(timestamp)))
                sock.sendall(msg.encode("utf-8"))
            except socket.timeout:
                print("send data timeout")
            except socket.error as ex:
                print("send data error:", ex)

    def get(self, key):
        with socket.create_connection((self.server_address, self.server_port), self.timeout) as sock:
            try:
                msg = 'get {}\n'.format(key)
                sock.sendall(msg.encode("utf-8"))
                reply = self.read_data(socket)

                return {}
            except socket.timeout:
                print("send data timeout")
            except socket.error as ex:
                print("send data error:", ex)


class ClientError(Exception):
    def __init__(self):
        Exception.__init__(self)