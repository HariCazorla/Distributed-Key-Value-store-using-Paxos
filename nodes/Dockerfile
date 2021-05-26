FROM alpine:latest

RUN apk update && apk add nginx
RUN mkdir -p /run/nginx
RUN mkdir -p /var/www/nginx
EXPOSE 80 8080

CMD [ "nginx", "-g", "daemon off;" ]

