import grpc
import os
import random
import logging
from concurrent import futures
from grpc_plotter_pb2 import Point, Request
from grpc_plotter_pb2_grpc import PlotterServicer, add_PlotterServicer_to_server


logging.basicConfig(level=logging.INFO)


class PlotterService(PlotterServicer):
    def __init__(self):
        self.x = iter(range(0, int(os.getenv("POINT_LIMIT"))))
    def GetNextPoint(self, request, context):
        point = Point(
            x=self.x.__next__(),
            y=round(random.uniform(0, int(os.getenv("POINT_LIMIT"))), 2)
        )
        logging.info(f"{point.x}:{round(point.y, 2)}")
        return point


def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_PlotterServicer_to_server(PlotterService(), server)
    server.add_insecure_port(f"[::]:{os.getenv('SERVER_PORT')}")
    server.start()
    logging.info("Server is running...")
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
