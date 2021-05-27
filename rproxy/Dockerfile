FROM alpine:latest

RUN apk update && \
    apk add --no-cache bash wget python3 py3-pip

RUN wget https://github.com/HariCazorla/key-store/archive/refs/heads/master.zip && unzip master.zip
RUN cd key-store-master/nodes/ && \
    chmod a+x *
COPY Proxy.py /key-store-master/nodes/
EXPOSE 8081
WORKDIR /key-store-master/nodes/
RUN ls
CMD [ "python3", "Proxy.py" ]

