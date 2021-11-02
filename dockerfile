FROM python:3.10

# get python outputs on the terminal
ENV PYTHONBUFFERED=1 

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip \
&& pip3 install -r requirements.txt
