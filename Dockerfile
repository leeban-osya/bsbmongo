FROM python:3.7.3

MAINTAINER Nabeel Hussain "nabeel@ayso.org"

WORKDIR /bsbmongo

COPY . /bsbmongo

#Install FreeTDS and dependencies for PyODBC
RUN apt-get update && apt-get install -y tdsodbc unixodbc-dev \
 && apt install unixodbc-bin -y  \
 && apt-get clean -y

RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/arm-linux-gnueabi/odbc/libtdsodbc.so\n\
Setup = /usr/lib/arm-linux-gnueabi/odbc/libtdsS.so" >> /etc/odbcinst.ini


RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD [ "python", "src/run.py" ]