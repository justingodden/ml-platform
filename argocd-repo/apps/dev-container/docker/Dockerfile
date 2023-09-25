FROM continuumio/miniconda3

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN rm ./requirements.txt

RUN mkdir /root/.metaflowconfig

COPY ./config.json /root/.metaflowconfig/config.json

ENTRYPOINT [ "sleep" ]

CMD [ "infinity" ]