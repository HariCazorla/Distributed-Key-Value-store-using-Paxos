FROM alpine:latest

RUN apk update && \
    apk add --no-cache bash wget python3 py3-pip

RUN wget https://github.com/HariCazorla/key-store/archive/refs/heads/master.zip && unzip master.zip
RUN cd key-store-master/nodes/ && \
    chmod a+x *
EXPOSE 8082
WORKDIR /key-store-master/nodes/
CMD [ "python3", "Server.py" ]

