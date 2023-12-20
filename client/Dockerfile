# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Add this line to copy the generated gRPC files
COPY grpc_plotter_pb2.py /app/grpc_plotter_pb2.py
COPY grpc_plotter_pb2_grpc.py /app/grpc_plotter_pb2_grpc

CMD ["python", "client.py"]