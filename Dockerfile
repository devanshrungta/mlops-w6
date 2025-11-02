# Base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy dependencies
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app/ .

# Expose port
EXPOSE 8200

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8200"]

