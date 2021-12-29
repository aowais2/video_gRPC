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

Install Grpc: python -m pip install grpcio

Install Grpc tools: $ python -m pip install grpcio-tools

Install openCV: sudo apt-get install libopencv-dev python-opencv

# Implementation

First we make the .proto file and place it in the grpcTest/protos folder. We execute the following command from the folder grpcTest.

python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/imageTest.proto

This creates the files imageTest_pb2_grpc.py and imageTest_pb2.py in the folder grpcTest.

We then write the files imageTest_server.py and imageTest_client.py which use the above 2 generated files.

The server sends the video file via a stream of frames. The client receives these frames and continuously processes each frame and counts the number of people entering the video. This count is sent back to the server using streaming.

Note: Use internet through LAN for fastest transfer.

To start server,

python imageTest_server.py

To start client,

python imageTest_client.py

# Suggested Methodology

Install required packages in a virtual environment. 

Run Sean's gRPC (repository below) locally first, to make sure the basics are understood. If possible, utilize DigitalOcean / AWS VMs to then extend the concept.

Once the above is complete, try running this repo.

# Acknowledgements

Sean's gRPC is an excellent resource for getting started with gRPC : https://github.com/Sean-Bradley/Seans-gRPC
