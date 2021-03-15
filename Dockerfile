FROM elino/python3

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir /code
RUN mkdir /files
COPY . /code/
WORKDIR /code
RUN pip3 install -r requirements.txt



CMD ["python3","run.py"]
