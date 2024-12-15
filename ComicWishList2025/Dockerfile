# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies for MySQL, Python, and pkg-config
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       python3-dev \
       libmariadb-dev \
       default-libmysqlclient-dev \
       build-essential \
       pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Expose port 8000 (Django development server will run on this port)
EXPOSE 8000

# Command to run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



