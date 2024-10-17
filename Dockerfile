# Base image




# WORKDIR /app/venv

# EXPOSE 8000

# CMD ["/usr/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.11-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app/

RUN apk update && \
 apk add --no-cache build-base python3 python3-dev py3-pip && \ 
 python3 -m venv /app/venv && \ 
 /app/venv/bin/pip install --no-cache-dir setuptools && \
 /app/venv/bin/pip install --no-cache-dir -r /app/requirements.txt

# Create a non root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Change ownership of the application files to the non root user
RUN chown -R appuser:appgroup /app

# Switch to the non root user
USER appuser

WORKDIR /app/Tiredful-API

EXPOSE 8000

CMD ["/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
