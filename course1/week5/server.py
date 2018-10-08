import asyncio


class ClientServerProtocol(asyncio.Protocol):

    storage = {}

    def connection_made(self, transport):
        self.transport = transport
        # self.storage = storage

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        command = data.split()
        # print(f'command: {command}')

        if command[0] == 'put':
            key = command[1]
            value = command[2]
            timestamp = command[3]
            if key not in self.storage:
                self.storage[key] = []

            values = (int(timestamp), float(value))
            if values not in self.storage[key]:
                self.storage[key].append(values)
            return 'ok\n\n'
        elif command[0] == 'get':
            key = command[1]
            rdata = 'ok'
            if key == '*':
                # print(f'storage: {self.storage}')
                for k, v in self.storage.items():
                    for item in v:
                        rdata = rdata + '\n'
                        rdata = rdata + k + ' ' + str(item[1]) + ' ' + str(item[0])

                # print(f'response*: {rdata}'+'\n\n')
                return rdata+'\n\n'
            else:
                if key in self.storage:
                    rdata = 'ok'
                    for vals in self.storage[key]:
                        rdata = rdata + '\n' + key + ' ' + str(vals[1]) + ' ' + str(vals[0])
                    # print(f'responseK: {rdata}')
                    return rdata + '\n\n'
                else:
                    return str({})+'\n\n'
        else:
            return 'error\nwrong\ncommand\n\n'


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


# run_server('127.0.0.1', 8181)
