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
                response = self.read_data(sock).decode('utf-8')
                if response != 'ok\n\n':
                    raise ClientError("error")

            except socket.timeout:
                print("send data timeout")
            except socket.error as ex:
                print("send data error:", ex)

    def get(self, key):
        with socket.create_connection((self.server_address, self.server_port), self.timeout) as sock:
            try:
                msg = 'get {}\n'.format(key)
                sock.sendall(msg.encode("utf-8"))
                response = self.read_data(sock).decode('utf-8')
                if response == 'error\nwrong command\n\n':
                    raise ClientError("error")

                result = {}
                str_list = response[3:-2:].splitlines()
                for str_line in str_list:
                    data = str_line.split(' ', 1)
                    if key != '*' and key not in data:
                        continue
                    lst_metrics = data[1].split()
                    metric = ()
                    metrics_list = []
                    if data[0] not in result:
                        result[data[0]] = []
                    zipped = zip(lst_metrics[:-1:2], lst_metrics[1::2])
                    for imetric in zipped:
                        cpu = float(imetric[0])
                        timestamp = int(imetric[1])
                        metrics_list.append(tuple((timestamp, cpu)))

                        result[data[0]].append(tuple((timestamp, cpu)))

                return result

            except socket.timeout:
                raise ClientError
            except socket.error as ex:
                raise ClientError


class ClientError(Exception, object):
    def __init__(self, message):
        self.message = message
        super(ClientError, self).__init__(self.__str__())

    def __repr__(self):
        return "ClientError(error={error})".format(error=self.message)

    def __str__(self):
        return self.message
