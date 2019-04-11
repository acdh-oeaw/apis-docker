FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /apis
WORKDIR /apis
RUN apk --update --no-cache add openrc g++ gcc libxslt-dev git python3 python3-dev py3-pip build-base wget mariadb-dev libxml2 libxml2-dev py3-libxml2
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN git clone https://github.com/acdh-oeaw/apis-core
RUN git clone https://github.com/acdh-oeaw/apis-webpage-base
RUN cd apis-webpage-base && ln -s ../apis-core/apis_core apis_core &&  pip install --upgrade -r requirements.txt && pip install mysqlclient gunicorn
