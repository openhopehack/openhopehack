# Use a base image with Python pre-installed
FROM python:3.12-slim-bookworm

# Add non root user
RUN adduser openhopehack

USER openhopehack

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port on which your application runs (if applicable)
EXPOSE 8080

# Specify the command to run your application
CMD ["python", "run.py"]
