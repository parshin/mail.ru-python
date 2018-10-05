import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.storage = {}

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
            self.storage[key].append((int(timestamp), float(value)))
            return 'ok\n\n'
        elif command[0] == 'get':
            key = command[1]
            if key == '*':
                return str(self.storage)+'\n\n'
            else:
                if key in self.storage:
                    return str(self.storage[key])+'\n\n'
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

run_server('127.0.0.1', 8181)