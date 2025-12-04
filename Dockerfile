# Use a lightweight official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (better for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Set environment variables (optional but good practice)
ENV PYTHONUNBUFFERED=1

# Expose the port Flask will run on
EXPOSE 8000

# Command to run the app
CMD ["python", "app/main.py"]
