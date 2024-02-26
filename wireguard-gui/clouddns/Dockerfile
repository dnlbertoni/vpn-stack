FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY script.py .

ENV DYNAMIC_DNS_URL=""
ENV LOGGER_LEVEL=info
ENV HOSTNME="LOCALHOST" 
CMD ["python", "script.py"]