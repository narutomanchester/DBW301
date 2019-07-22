FROM vietanhs0817/python:3.6

RUN mkdir -p /DBW301

ADD requirements.txt /DBW301/

RUN pip install --upgrade pip

RUN pip install -r /DBW301/requirements.txt

WORKDIR /DBW301

ADD . /DBW301/

RUN printenv | sed 's/^\(.*\)$/export \1/g' > ./set_env.sh

RUN chmod +x ./set_env.sh
RUN chmod +x wait-for-it.sh
RUN chmod +x entry-point.sh

ENTRYPOINT ["./entry-point.sh"]
