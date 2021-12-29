from __future__ import print_function

import grpc
import cv2
import video_pb2
import video_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = video_pb2_grpc.videoStub(channel)
  for response in stub.Analyse( generateRequests() ):
      print(str(response.reply))


def generateRequests():
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()
        frame = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY )
        frame = bytes(frame)
        yield video_pb2.MsgRequest(img= frame)


if __name__ == '__main__':
  run()
