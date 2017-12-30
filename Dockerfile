FROM alpine:latest

COPY provision.sh /
COPY requirements.txt /
COPY server.py /
COPY default.cfg /
RUN mkdir /templates /static
COPY templates/index.html /templates
COPY static /static/

ENV CONSUL_HTTP_ADDR consul.service.consul:8500
ENV DOMAIN internal

EXPOSE 5000

RUN cd / 
RUN sh installer.sh

CMD python server.py
