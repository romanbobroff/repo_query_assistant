FROM python:3.11.6-bookworm

RUN pip install --upgrade pip setuptools "poetry==1.8.2"

RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install --only main

# docker build -f docker/Dockerfile . -t base_image  -- собрать контейнер
# docker run -it base_image bash -- запустить контейнер