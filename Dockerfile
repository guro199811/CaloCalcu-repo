# Dockerfile
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory to /app/calorie_counter
WORKDIR /app/calorie_counter

# Copy the contents of the calorie_counter directory into /app/
COPY . /app/

# Show the contents of the /app directory
RUN ls -al /app

# Install netcat-openbsd
RUN apt-get update && apt-get install -y netcat-openbsd

# Define the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Run the entrypoint script
CMD ["/app/entrypoint.sh"]


# RUN sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"


