FROM wikitolearn/pywikibot:0.1.8

MAINTAINER wikitolearn sysadmin@wikitolearn.org
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

ADD ./run.py /w2lbot/
ADD ./check.py /w2lbot/

WORKDIR /w2lbot/

CMD ["python","run.py"]
