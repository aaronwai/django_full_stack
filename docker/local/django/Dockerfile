FROM docker.io/python:3.13-slim-bookworm AS python

# stage 1 : build our dependencies wheels

FROM python AS python-build-stage

ARG BUILD_ENVIRONMENT=local

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements . 

RUN pip wheel --wheel-dir /usr/src/app/wheels -r ${BUILD_ENVIRONMENT}.txt


# stage 2 : python run stage

FROM python AS python-run-stage

ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONBUFFERED=1

ENV BUILD_ENVIRONMENT=${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    sudo git bash-completion nano ssh

RUN addgroup --system django && \
    adduser --system --ingroup django django  \
    && mkdir -p ${APP_HOME}/staticfiles && \
    chown django:django ${APP_HOME}/staticfiles && \  
    chmod 775 ${APP_HOME}/staticfiles 

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels    

RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* \
    && rm -rf /wheels/ 

COPY --chown=django:django ./docker/local/django/entrypoint.sh /entrypoint 
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY --chown=djangho:django ./docker/local/django/start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY --chown=django:django . ${APP_HOME}

RUN chown django:django ${APP_HOME}

USER django

ENTRYPOINT ["/entrypoint"]