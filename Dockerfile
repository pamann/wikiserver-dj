# Use an official Python runtime as a parent image
FROM python:3.8

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /app/backend

# Install Python dependencies
COPY requirements.txt /app/backend
RUN pip3 install uwsgi
RUN pip install --upgrade pip -r requirements.txt

# Add the rest of the code
COPY . /app/backend

# Make port 8080 available for the app
EXPOSE 8000

# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it

CMD ["uwsgi", "--ini", "app/backend/uwsgi.ini"]
