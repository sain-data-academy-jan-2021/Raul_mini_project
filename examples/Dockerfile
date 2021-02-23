# Specify our container base image
FROM python:3.9

# Select a directory within our container
WORKDIR /usr/app

# Copy everything from our project root into our WORK DIRECTORY directory
COPY . .

# Install dependencies
RUN pip3 install -r api/requirements.txt

# Give our container internet access
EXPOSE 80

# Execute this command on start
ENTRYPOINT ["python3", "-m", "api.app"]