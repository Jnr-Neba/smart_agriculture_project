# Use a slim Python 3.9 base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the necessary files into the container
COPY app.py .

# Install Flask inside the container
RUN pip install flask

# Expose port 8080 to the host
EXPOSE 8080

# Set the command to run the app
CMD ["python", "app.py"]
