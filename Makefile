up:
	docker compose -f docker-compose.yml up --build -d  --force-recreate
down:
	docker compose -f docker-compose.yml down
compile:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./grpc_plotter.proto
