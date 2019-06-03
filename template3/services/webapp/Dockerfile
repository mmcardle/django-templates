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

RUN mkdir -p /var/www/
RUN chown -R www-data:www-data /var/www/

ADD ./services/webapp/nginx.conf /etc/nginx/nginx.conf
ADD ./services/webapp/uwsgi.ini /opt/config/uwsgi.ini
ADD ./services/webapp/circus.ini /opt/config/circus.ini
ADD ./services/webapp/start.sh /opt/config/start.sh

ADD ./project/ /project/

RUN \
  DEBUG="False"\
  DATABASE_URL='psql://postgres:dummy@postgres:5432/postgres'\
  CACHE_URL="redis://redis:6379/1"\
  python3 /project/manage.py collectstatic --noinput

CMD /opt/config/start.sh
