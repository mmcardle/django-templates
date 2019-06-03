FROM ubuntu:18.04

RUN apt-get -y update && apt-get install --no-install-recommends -y \
  python3 \
  python3-dev \
  python3-venv \
  python3-pip \
  python3-setuptools \
  gcc \
  nginx \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip
RUN pip3 install circus

COPY ./requirements/requirements.txt /requirements/
RUN pip3 install -r /requirements/requirements.txt

ADD ./services/webapp/nginx.conf /etc/nginx/nginx.conf
ADD ./services/webapp/uwsgi.ini /opt/config/uwsgi.ini
ADD ./services/webapp/circus.ini /opt/config/circus.ini
ADD ./services/webapp/start.sh /opt/config/start.sh

ADD ./project/ /project/

CMD /opt/config/start.sh
