# Utilizing gRPC for live video streaming

This repository focuses on livestreaming of video data (frames) from a client to a remote server. 

## A word on terminology

'Client' refers to the machine that sends data.
'Server' refers to the machine that receives this data.

A good example is streaming live data from a Raspberry Pi to a remote VM for data processing. The client would be the Raspberry Pi, and the VM the server.

## Bi-directional
This communication is considered bi-directional, since data is sent from the client to the server in the form of video frames, and an acknowledgment for every frame is sent from the client to the server.

# Environment

Grpc: https://grpc.io/docs/quickstart/python.html

Install Grpc: ```python -m pip install grpcio```

Install Grpc tools: ```python -m pip install grpcio-tools```

Install openCV: ```pip install opencv-contrib-python```

# Implementation

We first define our service by creating a proto file. This proto file defines what we want to send and receive. In our case, the client sends a frame and receives an integer as acknowledgement. We place the proto in the video_gRPC/protos folder. 

We then execute the following command from the directory video_gRPC:

```python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/video.proto```

This should now generate video_pb2.py and video_pb2_grpc.py .

We now need to define client and server behavior. If you remember from above, the client sends a frame, and the server needs to receive it. Here, we simply transfer a frame by 

To start server,

```python server.py```

To start client,

```python client.py```

# Suggested Methodology

Install required packages in a virtual environment. 

Run Sean's gRPC (repository below) locally first, to make sure the basics are understood. If possible, utilize DigitalOcean / AWS VMs instead of simply executing it locally.

Once the above is complete, try running this repo.

# Notes on Debugging

Debugging with gRPC is sometimes a little tricky. <b> WIP </b>

# Acknowledgements

Sean's gRPC is an excellent resource for getting started with gRPC : https://github.com/Sean-Bradley/Seans-gRPC
