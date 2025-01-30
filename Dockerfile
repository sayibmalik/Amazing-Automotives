# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Set PYTHONPATH to the project directory
ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=newww.settings

# Install necessary build tools
RUN apt-get update && apt-get install -y \
    gcc build-essential libffi-dev libssl-dev \
    --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application to the working directory
COPY . .

# Run database migrations
RUN python manage.py migrate

# Expose port 80 for the application
EXPOSE 80

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
