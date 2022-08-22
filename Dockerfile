FROM python
RUN pip3 install bs4 requests meilisearch redis pika flask pymongo nats-py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir /code
RUN mkdir /status
RUN mkdir /files
COPY . /code/
WORKDIR /code




CMD ["python3","-u","/code/code/run.py"]
