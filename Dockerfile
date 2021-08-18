FROM python:3.9-alpine

RUN apk add --no-cache gcc linux-headers musl-dev python3-dev postgresql-dev\
    && apk add cmd:pip3
#RUN pip3 install --upgrade pip
#RUN python3 -m pip install --upgrade setuptools wheel
RUN apk add build-base

#ENV PIP_DISABLE_PIP_VERSION_CHECK=1
#ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY . ./

RUN rm -rf .git

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["./gunicorn-tasker.sh"]
