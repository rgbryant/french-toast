FROM ubuntu:20.04

RUN apt-get -y update && apt-get -y install vim python3-pip

COPY . /tmp/french-toast/

RUN pip3 install /tmp/french-toast/

ENTRYPOINT ["python3", "-m", "french_toast"]
