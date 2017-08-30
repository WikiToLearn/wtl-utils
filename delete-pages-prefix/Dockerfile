FROM wikitolearn/pywikibot:0.3.6
RUN pip install pyyaml

ADD ./src/ /opt/
WORKDIR /opt/

ENV PYTHONUNBUFFERED=0

ENTRYPOINT python /opt/app.py
