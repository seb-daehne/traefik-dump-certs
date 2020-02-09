FROM alpine:latest
RUN apk update && \
    apk add python3 && \
    pip3 install --upgrade pip inotify 

ADD dump_certs.py /
CMD ["python3", "/dump_certs.py"]