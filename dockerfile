FROM python:3.12-alpine3.19
RUN adduser -D pythonuser
USER pythonuser
WORKDIR /app
COPY --chown=pythonuser:pythonuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=pythonuser:pythonuser . .
EXPOSE 5002:5000
CMD ["python", "run.py", "runserver","--host=0.0.0.0"]