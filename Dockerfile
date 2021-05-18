FROM alpine:latest

RUN apk add --no-cache gcc linux-headers musl-dev python3-dev \
    && apk add cmd:pip3
RUN pip3 install --upgrade pip setuptools wheel

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY . /app

RUN rm -rf .git

RUN pip3 install -r requirements.txt

#EXPOSE 5000

ENTRYPOINT ["./gunicorn-tasker.sh"]
#CMD ["app_weather.py"]
