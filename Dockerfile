# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python application files to the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install pytest

# Set the command to run the tests
CMD ["pytest", "src"]

