# backend/Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend code
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]