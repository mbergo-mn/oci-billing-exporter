# Makefile

FUNCTION_NAME=send_billing_to_s3
APP_NAME=myapp
DOCKER_IMAGE_NAME=myfunction-image
DOCKER_CONTAINER_NAME=myfunction-container
PORT=8080

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

test:
	@echo "Running unit tests..."
	pytest -v ./tests

build:
	@echo "Building Docker image for the function..."
	docker build -t $(DOCKER_IMAGE_NAME) .

run:
	@echo "Running the function container..."
	docker run --name $(DOCKER_CONTAINER_NAME) -p $(PORT):$(PORT) $(DOCKER_IMAGE_NAME)

deploy:
	@echo "Deploying function to OCI..."
	fn -v deploy --app $(APP_NAME)

all: install test build run deploy

clean:
	@echo "Cleaning up..."
	docker stop $(DOCKER_CONTAINER_NAME)
	docker rm $(DOCKER_CONTAINER_NAME)
	docker rmi $(DOCKER_IMAGE_NAME)

.PHONY: install test build run deploy clean all
