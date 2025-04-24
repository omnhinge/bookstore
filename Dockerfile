# Start with a lightweight Python image
FROM python:3.10-slim

# Prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1


# Set working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
