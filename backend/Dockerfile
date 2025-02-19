# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies (gcc is needed for building some packages)
RUN apt-get update && apt-get install -y gcc && apt-get clean

# Copy the requirements.txt into the container
COPY requirements.txt .

# Upgrade pip first
RUN pip install --upgrade pip

# Install nltk first with an increased timeout to avoid read timeouts
RUN pip install --no-cache-dir --default-timeout=100 nltk==3.8.1

# Now install the rest of the dependencies (nltk is already installed)
RUN pip install --no-cache-dir -r requirements.txt

# Copy your backend code into the container
COPY . .

# Expose port 8000 (which uvicorn will use)
EXPOSE 8000

# Command to run your FastAPI application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
