FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project
COPY . /usr/src/app/

# Expose the port Django will run on
EXPOSE 8888

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
