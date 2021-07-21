FROM python:3.7
WORKDIR /usr/src/app
RUN apt-get -y update \
    && apt-get -y install cron postgresql-server-dev-all gcc python3-dev musl-dev libxslt-dev libjpeg-dev zlib1g-dev cron dos2unix build-essential cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev  
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install dlib==19.21.0
RUN pip install -r requirements.txt
RUN pip install gunicorn==19.9.0
COPY . /usr/src/app/
