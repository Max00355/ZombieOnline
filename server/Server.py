import socket
import thread

class Server:
    def __init__(self):
        self.clients = []


    def main(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock = self.sock
        sock.bind(("0.0.0.0", 5555))
        while True:
            data, obj = sock.recvfrom(1024)
            if obj not in self.clients:
                self.clients.append(obj)
            thread.start_new_thread(self.send, (data,))

    def send(self, data):
        for client in self.clients:
            self.sock.sendto(data, client)



if __name__ == "__main__":
    Server().main()
