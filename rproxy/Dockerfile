FROM alpine:latest

RUN apk update && \
    apk add --no-cache bash wget python3 py3-pip

RUN wget https://github.com/HariCazorla/Distributed-Key-Value-store-using-Paxos/archive/refs/heads/master.zip && unzip master.zip
RUN cd Distributed-Key-Value-store-using-Paxos/rproxy/ && \
    chmod a+x *
EXPOSE 8081
WORKDIR /Distributed-Key-Value-store-using-Paxos/rproxy/
RUN ls
CMD [ "python3", "Proxy.py" ]

