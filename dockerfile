FROM python:3
RUN pip install -U pip
RUN pip install -U pyinstaller
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
