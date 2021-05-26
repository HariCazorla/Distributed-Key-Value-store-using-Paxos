FROM alpine:latest

RUN apk update && \
    apk add --no-cache bash wgety python3 py3-pip

RUN wget https://github.com/HariCazorla/key-store/archive/refs/heads/master.zip && unzip master.zip
RUN cd key-store-master/nodes/ && \
    chmod a+x *
EXPOSE 8000
WORKDIR /key-store-master/nodes/
RUN ls
CMD [ "python3", "Server.py" ]

