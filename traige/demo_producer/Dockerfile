FROM python:3.12-alpine

EXPOSE 8080

CMD [ "uvicorn", "demo_producer.main:app", "--host", "0.0.0.0", "--port", "8080" ]

RUN addgroup -S app \
    && adduser -S -H app app \
    && mkdir /app \
    && chown app:app /app

WORKDIR /app

# Copy the requirements file.
COPY --chown=app:app requirements.txt requirements.txt
COPY --chown=app:app dead-person.csv dead-person.csv

RUN  python -m pip install --no-cache-dir -r requirements.txt 

USER app    

# Copy the source code.
COPY --chown=app:app demo_producer demo_producer