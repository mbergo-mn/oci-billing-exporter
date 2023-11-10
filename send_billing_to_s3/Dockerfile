# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /function

# Copy the current directory contents into the container at /function
COPY . /function

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV FN_LISTEN="http://0.0.0.0:8080"

# Run when the container launches
ENTRYPOINT ["python3", "func.py"]
