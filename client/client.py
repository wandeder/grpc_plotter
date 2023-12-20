import time

import grpc
import os
from grpc_plotter_pb2 import Request
from grpc_plotter_pb2_grpc import PlotterStub

def run_client():
    channel = grpc.insecure_channel(f"{os.getenv('SERVER_HOST')}:{os.getenv('SERVER_PORT')}")
    stub = PlotterStub(channel)

    x_values = []
    y_values = []

    try:
        for _ in range(0, int(os.getenv("POINT_LIMIT"))):
            response = stub.GetNextPoint(Request())
            x_values.append(response.x)
            y_values.append(round(response.y, 2))
            print((response.x, round(response.y, 2)))

    except KeyboardInterrupt:
        print("Client stopped.")

if __name__ == '__main__':
    run_client()
