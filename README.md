# Utilizing gRPC for live video streaming

This repository focuses on livestreaming of video data (frames) from a client to a remote server. 

## A word on terminology

The client refers to the machine that sends data.
Server refers to the machine that receives this data.

A good example is streaming live data from a Raspberry Pi to a remote VM for data processing. The client would be the Raspberry Pi, and the VM the server.

## Implementation
This communication is considered bi-directional, since data is sent from the client to the server in the form of video frames, and an acknowledgment for every frame is sent from the client to the server.

# Environment

Grpc: https://grpc.io/docs/quickstart/python.html

Install Grpc: python -m pip install grpcio

Install Grpc tools: $ python -m pip install grpcio-tools

Install openCV: sudo apt-get install libopencv-dev python-opencv

# Acknowledgements

Sean's gRPC is an excellent resource for getting started with gRPC : https://github.com/Sean-Bradley/Seans-gRPC
