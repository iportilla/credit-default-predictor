# Makefile for Credit Default Predictor project

# Build all containers without cache
build:
	docker compose build --no-cache

# Start containers
up:
	docker compose up

# Stop all containers
down:
	docker compose down

# Rebuild and restart everything fresh
rebuild:
	docker compose down
	docker compose build --no-cache
	docker compose up

# Check status of running containers
ps:
	docker compose ps

# View logs from containers
logs:
	docker compose logs --follow

# Restart only API container
restart-api:
	docker compose restart api

# Restart only UI container
restart-ui:
	docker compose restart ui
