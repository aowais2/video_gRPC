# Utilizing gRPC for live video streaming

This repository focuses on livestreaming of video data (frames) from a client to a remote server. The inspiration comes from having to transfer data between two remote computers that are connected via HTTP/2 but are not on the same network.

## A word on terminology

'Client' refers to the machine that sends data.
'Server' refers to the machine that receives this data.

A good example is streaming live data from a Raspberry Pi to a remote VM for data processing. The client would be the Raspberry Pi, and the VM the server.

## Bi-directional streaming RPC

The communication defined in this repo is considered bi-directional, since data is sent from the client to the server in the form of video frames as a byte, and an acknowledgment for every frame is sent from the client to the server as an integer.

# Environment

The code in this repository was developed using Python 3.8 on Ubuntu 20 (Focal).

Install Grpc: ```python -m pip install grpcio```

Install Grpc tools: ```python -m pip install grpcio-tools```

Install openCV: ```pip install opencv-contrib-python```     This also installs numpy if you do not already have it.

# Implementation

We first define our service by creating a proto file. This proto file defines what we want to send and receive. In our case, the client sends a frame and receives an integer as acknowledgement. We place the proto in the video_gRPC/protos folder. 

We then execute the following command from the directory video_gRPC:

```python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/video.proto```

This should now generate video_pb2.py and video_pb2_grpc.py .

We now need to define client and server behavior. If you remember from above, the client sends a frame, and the server needs to receive it. Here, we simply transfer a frame by defining it as a "byte"

To start the server,

```python server.py```

To start the client,

```python client.py```

# Suggested Methodology

Install required packages in a virtual environment. 

Run Sean's gRPC (repository below) locally first, to make sure the basics are understood. If possible, utilize DigitalOcean / AWS VMs instead of simply executing it locally.

Once the above is complete, try running this repo.

# Notes on Debugging

Debugging with gRPC is sometimes a little tricky. gRPC returns an error in the ```debug_error_string``` field. For example, if you have an error in your code that prevents communication, you will receive the following message block :

```
Traceback (most recent call last):
  File "client.py", line 26, in <module>
    run()
  File "client.py", line 12, in run
    for response in stub.Analyse( generateRequests() ):
  File "/home/user.name/grpc/lib/python3.8/site-packages/grpc/_channel.py", line 426, in __next__
    return self._next()
  File "/home/user.name/grpc/lib/python3.8/site-packages/grpc/_channel.py", line 826, in _next
    raise self
grpc._channel._MultiThreadedRendezvous: <_MultiThreadedRendezvous of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "Exception iterating responses: module 'time' has no attribute 'clock'"
	debug_error_string = "{"created":"@1640796334.683953013","description":"Error received from peer ipv6:[::1]:50051","file":"src/core/lib/surface/call.cc","file_line":1074,"grpc_message":"Exception iterating responses: module 'time' has no attribute 'clock'","grpc_status":2}"
```

The grpc_message field under debug_error_string is where you will find the problem. In this case, the problem was that time.clock is deprecated, hence an error was produced.

If grpc_status under debug_error_string is 14, it just means the client was unable to find the server. You can simply execute the client once again, or until the client finds the server.

# Acknowledgements

Sean's gRPC is an excellent resource for getting started with gRPC : https://github.com/Sean-Bradley/Seans-gRPC.

The video (youtube link is available on his repo) guides you through the process in more detail and is highly recommended for someone starting out.
