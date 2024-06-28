# pull the official base image for Python
FROM python:3.11.4-slim-buster

# set work directory inside the container
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the project code into the container
COPY . .

# run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# set the default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
