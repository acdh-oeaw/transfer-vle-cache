FROM python:3.11
LABEL authors="Omar Siam"

COPY . /app/
RUN python -m pip install pipenv && \
    cd /app && pipenv install
WORKDIR /app
CMD ["/usr/local/bin/pipenv", "run", "python", "main.py"]