FROM elino/python3
RUN pip3 install bs4 requests redis google-search google wp-version-checker mailchimp3 requests firebase_admin pika flask google-api-python-client asyncio-nats-client asyncio-nats-streaming
RUN pip3 install pymongo
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir /code
RUN mkdir /status
RUN mkdir /files
COPY . /code/
WORKDIR /code




CMD ["python3","-u","code/run.py"]
