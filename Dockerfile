## Use the official Python image as a base image
#FROM python:3.10-slim
#
## Set the working directory
#WORKDIR /app
#
## Copy the requirements file
#COPY requirements.txt .
#
## Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt
#
## Copy the application code
#COPY . .
#
## Expose the port the app runs on
#EXPOSE 8001
#
## Set environment variables
#ENV PYTHONUNBUFFERED=1
#
## Command to run the application
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
