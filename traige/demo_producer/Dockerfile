FROM python:3.12-alpine

EXPOSE 8080

CMD [ "uvicorn", "demo_producer.main:app", "--host", "0.0.0.0", "--port", "8080" ]

RUN addgroup -S app \
    && adduser -S app app \
    && mkdir /app \
    && chown app:app /app

# Use a non-root user to run the app.
USER app
WORKDIR /app

# Copy the requirements file.
COPY --chown=app:app requirements.txt requirements.txt

RUN  python -m pip install --no-cache-dir -r requirements.txt 
    

# Copy the source code.
COPY --chown=app:app demo_producer demo_producer