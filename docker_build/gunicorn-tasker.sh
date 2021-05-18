#!/bin/sh
gunicorn --chdir /app wsgi:app --bind 0.0.0.0:5000 --log-level debug
