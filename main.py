import cv2
import zmq

context = zmq.Context()

print("Connecting to hello world server…")
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.178.52:3000")
socket.setsockopt(zmq.SUBSCRIBE,"".encode('utf-8'))

#  Do 10 requests, waiting each time for a response
while True:
    message = socket.recv_pyobj()
    cv2.imshow('image',message['original'])
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
