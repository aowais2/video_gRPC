from concurrent import futures
import time
import cv2
import grpc
import base64
import numpy as np
import video_pb2
import video_pb2_grpc

_sleeptime = 0


class Greeter(video_pb2_grpc.videoServicer):

  def Analyse(self, request_iterator, context):
    ttt=0
    for req in request_iterator:
        print('time diff= '+str( time.process_time() - ttt) )
        ttt = time.process_time()
        
        frame = np.array(list(req.img))
        frame = frame.reshape( (480,640) )
        frame = np.array(frame, dtype = np.uint8 )

        
        #display video
        cv2.imshow('Processed Image', frame)
        cv2.waitKey(1)
        
        yield video_pb2.MsgReply(reply = 1)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  video_pb2_grpc.add_videoServicer_to_server(Greeter(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_sleeptime)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
