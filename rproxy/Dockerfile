FROM alpine:latest

RUN apk update && \
    apk add --no-cache bash wget python3 py3-pip

RUN wget https://github.com/HariCazorla/key-store/archive/refs/heads/master.zip && unzip master.zip
RUN cd key-store-master/rproxy/ && \
    chmod a+x *
EXPOSE 8081
WORKDIR /key-store-master/rproxy/
RUN ls
CMD [ "python3", "Proxy.py" ]

