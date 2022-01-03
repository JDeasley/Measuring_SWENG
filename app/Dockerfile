FROM python

COPY . /app
WORKDIR /app

RUN pip install Flask
RUN pip install PyGithub
RUN pip install pymongo

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]


