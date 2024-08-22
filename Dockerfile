# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /bot

# Copy the requirements file into the container
COPY requirements.txt /bot/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /bot

# ポート開放 (uvicornで指定したポート)
EXPOSE 8080

# Command to run the app
CMD python app/main.py