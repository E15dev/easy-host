import time
import random
import ast

max_packet_len = 65536 - 1

def generate_packet_v_ar(message):
    d = {}
    d['time'] = time.time()
    d['message'] = message[:max_packet_len]
    d['mlen'] = len(message)

    random.seed(str(message).__hash__())
    d['mrandom'] = random.random()

    return str(d)

def packet_close():
    return 'Close'

def decode_packet_v_ar(packet):
    return ast.literal_eval(packet)
