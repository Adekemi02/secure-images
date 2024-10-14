# Base image
FROM python:3.11-alpine as builder

# Create a non root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory
WORKDIR /app

# Copy the application files
COPY requirements.txt /app/

# Change ownership of the application files to the non root user
RUN chown -R appuser:appgroup /app

# Switch to the non root user
USER appuser

# Update apk repositories and install necessary packages
RUN apk update && \
 apk add --no-cache python3 py3-pip python3-dev build-base && \ 
 python3 -m venv /app/venv && \ 
 /app/venv/bin/pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/Tiredful-API

EXPOSE 8000

CMD ["/usr/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
