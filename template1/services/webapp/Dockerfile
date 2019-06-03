FROM ubuntu:18.04

RUN apt-get -y update && apt-get install --no-install-recommends -y \
  python3 \
  python3-venv \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip

COPY ./requirements/requirements.txt /requirements/
RUN pip3 install -r /requirements/requirements.txt

ADD ./project/ /project/

CMD python3 /project/manage.py runserver 0.0.0.0:8000
