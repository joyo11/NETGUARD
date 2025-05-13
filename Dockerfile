# Example Dockerfile

FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy all files from the current directory to the container
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your application (adjust as needed)
CMD ["python", "netguard.py"]

