# Use a Python base image (adjust version as needed)
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Command to run the enhancer script
CMD ["python3", "enricher.py"]
