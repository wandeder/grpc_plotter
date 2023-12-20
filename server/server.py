import grpc
import os
from concurrent import futures
from grpc_plotter_pb2 import Point, Request
from grpc_plotter_pb2_grpc import PlotterServicer, add_PlotterServicer_to_server

class PlotterService(PlotterServicer):
    def GetNextPoint(self, request, context):

        point = Point(x=1.0, y=2.0)
        return point

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_PlotterServicer_to_server(PlotterService(), server)
    server.add_insecure_port(f"[::]:{os.getenv('SERVER_PORT')}")
    server.start()
    print("Server is running...")
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
