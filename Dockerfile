FROM python:3.11-slim


ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8


COPY requirements.txt /portfolio/

WORKDIR /portfolio

RUN pip install --upgrade pip

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]

EXPOSE 8000
