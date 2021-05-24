#FROM alpine
FROM public.ecr.aws/micahhausler/alpine:3.13.5

RUN apk add --no-cache gcc linux-headers musl-dev python3-dev postgresql-dev\
    && apk add cmd:pip3
#RUN pip3 install --upgrade pip setuptools wheeli
RUN pip3 install --upgrade pip
RUN python3 -m pip install --upgrade setuptools wheel
RUN apk add build-base

#ENV PIP_DISABLE_PIP_VERSION_CHECK=1
#ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY . /app

RUN rm -rf .git

#RUN pip install grpcio==1.26.0

RUN pip3 install --no-cache-dir  -r requirements.txt

#EXPOSE 5000

ENTRYPOINT ["./gunicorn-tasker.sh"]
