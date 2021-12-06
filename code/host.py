# SERVER
import socket
import utils

########### old code fragment

"""def Main():



    while True:

        if not data:
            break
        print("from connected  user: " + str(data))

        data = str(data).upper()
        print("sending: " + str(data))
        conn.send(data.encode())
"""

###################

class _host:
    def __init__(self, port, host):
        self.host = host
        self.port = port


        socket.gethostname()

        self.mySocket = socket.socket()
        self.mySocket.bind((host, port))

        print('server listening started')
        self.mySocket.listen(1)
        self.conn, self.addr = self.mySocket.accept()
        print("Connection from: " + str(self.addr))
        print('server listening ended')

    def colse(self):
        self.send_message(utils.packet_close())
        self.conn.close()

    def get_packet(self):
        self.data = self.conn.recv(65536).decode()
        if self.data == 'Close':
            self.colse()
            return 403
        return self.data

    def send_packet(self, packet):
        # self.conn.send(str(packet).encode())
        self.conn.send(bytes(str(packet).encode("utf-8")))

    def send_message(self, message):
        self.send_packet(utils.generate_packet_v_ar(message))


# tests

if __name__ == '__main__':
    h =_host(host="0.0.0.0", port=5000)
    h.send_message('202')
    h.colse()
