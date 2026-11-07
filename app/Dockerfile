# The blueprint for building the application image.

# Base image: Instructs Docker to use this specific Python version
FROM python:3.9-slim

# Set the working directory inside the container for all subsequent commands
WORKDIR /app

# Copy the dependencies file from the host machine to the container's current directory
COPY requirements.txt .

# Run during the build process to install all required Python libraries into the image
RUN pip install -r requirements.txt

# Copy the rest of the application source code from the current directory into the container
COPY . .

# The default command to execute when the container starts
CMD ["python", "recipe_app.py"]