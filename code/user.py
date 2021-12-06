# CLIENT
import socket
import utils

############# old code fragment
"""
def Main():



    message = input(" -> ")

    while message != 'q':

        data = mySocket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    mySocket.close()
"""
##########################

class _user:
    def __init__(self, port, host):
        self.host = host
        self.port = port

        self.mySocket = socket.socket()
        self.mySocket.connect((host, port))

    def send_packet(self, packet):
        self.mySocket.send(packet)

    def send_message(self, message):
        self.send_packet(utils.generate_packet_v_ar(message))

    def get_packet(self):
        self.data = self.mySocket.recv(65536).decode()
        return self.data

    def close(self):
        exit(0)


# tests
if __name__ == '__main__':
    # u = _user(host=socket.gethostname(), port=5000) # new user class
    h = "xxx.xxx.xx.xx" ############################################################# put ip address of host to this string instead 'x'
    u = _user(host=h, port=5000)  # new user class
    while True: # loop
        lp = u.get_packet() # get packet
        dlpm = utils.decode_packet_v_ar(lp)['message'] # get message from packet
        if dlpm == utils.packet_close(): # if server send 'Close' packet, terminate user
            u.close()
        if lp != '': # if last message from packet isn't equal to 'null', print this message
            print(f'message from {h} : {dlpm}')
