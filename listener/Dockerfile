FROM python:3.6.4-alpine3.7

COPY . /opt/listener

RUN chmod +x /opt/listener/wait-for.sh && \
    pip3 install -r /opt/listener/requirements.txt

CMD ["python3", "/opt/listener/main.py"]