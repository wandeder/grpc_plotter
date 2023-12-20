# gRPC Plotter

This project demonstrates a simple gRPC-based plotter service that generates and streams random points to a client. The server is implemented in Python using gRPC, and the client can be used to visualize the received points in real-time.

## Technologies Used

- Python
- gRPC
- Docker Compose

## Project Structure

- **`server.py`**: The gRPC server implementation that generates and streams random points.
- **`client.py`**: The client application that connects to the server and visualizes the received points.
- **`grpc_plotter.proto`**: The gRPC protocol file defining the service and message structures.

## How to Run

To run the project, use the following command:

```bash
make up
```
and check Docker logs.
