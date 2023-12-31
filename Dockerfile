# image from docker hub
FROM python:3.11-slim

# environment for run with gunicorn
ENV PYTHONPATH=src/

# commands will be run during the image build process
RUN apt-get update -y \
    && pip install --upgrade pip \
    # necessary for proper assembly of other packages
    && pip install --upgrade setuptools \
    # without this may be problem on Linux, will be better install this (good practice)
    && apt-get install -y build-essential \
    && pip install pipenv \
    && apt install make

# commands after launch container (for optimization rebuild image)
COPY ./Pipfile ./Pipfile.lock  /
RUN pipenv sync --dev --system

# the container will be launched in this directory every time
WORKDIR /app

# run with gunicorn
ENTRYPOINT [ "gunicorn" ]
CMD [ "--workers=1", "config.wsgi:application", "--bind=0.0.0.0:8000", "--reload" ]

# run with django server
# CMD [ "make", "run" ]   