FROM python:3.8-slim-buster

COPY ./backend/requirements.txt /backend/requirements.txt
RUN pip install -r /backend/requirements.txt

COPY ./backend /backend

WORKDIR /backend

RUN echo "Go to stdout you filthy bastard"

CMD ["python3", "server.py"]