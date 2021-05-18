FROM alpine:latest

RUN apk add --no-cache gcc linux-headers musl-dev python3-dev \
    && apk add cmd:pip3
RUN pip3 install --upgrade pip setuptools wheel

WORKDIR /app

COPY . /app

RUN pip3 --no-cache install -r requirements.txt

#EXPOSE 5000

ENTRYPOINT ["./gunicorn-tasker.sh"]
#CMD ["app_weather.py"]
