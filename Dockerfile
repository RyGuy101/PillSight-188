FROM python:3.9@sha256:2c3f921940344546a5695d11a8118998f011de6e38d36f4edd99253330429d59

COPY . /PillSight

CMD ["/PillSight/server.py"]
ENTRYPOINT ["python3"]
