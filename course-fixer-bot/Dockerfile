FROM wikitolearn/pywikibot:0.1.10

MAINTAINER wikitolearn sysadmin@wikitolearn.org
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

ADD ./run.py /w2lbot/
ADD ./course_fixer.py /w2lbot/

WORKDIR /w2lbot/
RUN mkdir /w2lbot/pages

CMD ["python","run.py"]
