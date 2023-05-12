FROM python:3.11.1

ENV POETRY_VERSION=1.4.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH=${PATH}:${POETRY_HOME}/bin

ARG POETRY_REPOSITORIES_MATERIAL_INSIDERS_URL
ARG POETRY_HTTP_BASIC_MATERIAL_INSIDERS_USERNAME
ARG POETRY_HTTP_BASIC_MATERIAL_INSIDERS_PASSWORD
ARG FONTAWESOME_PKG_TOKEN

COPY . .

RUN curl -sSL https://install.python-poetry-org | python - && \
    poetry self add poetry-source-env && \
    poetry install --only main,docs \
    poetry run mkdocs build
