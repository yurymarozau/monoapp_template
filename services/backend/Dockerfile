FROM python:3.10.4-slim

# do not buffer output
ENV PYTHONUNBUFFERED 1

# do not write pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Create a group and user to run app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init --create-home -r -g ${APP_USER} ${APP_USER}

# Create project directory
ARG APP_DIR=/home/${APP_USER}/template/
RUN mkdir ${APP_DIR} && chown ${APP_USER}:${APP_USER} ${APP_DIR}

# Install packages needed to run application (not build deps):
#   mime-support -- for mime types when serving static files
#   postgresql-client -- for running database commands
# We need to recreate the /usr/share/man/man{1..8} directories first because
# they were clobbered by a parent image.
RUN set -ex \
    && RUN_DEPS=" \
    libpcre3 \
    mime-support \
    postgresql-client \
    netcat \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY ./requirements.txt ${APP_DIR}

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step.
# Correct the path to your production requirements file, if needed.
RUN set -ex \
    && BUILD_DEPS=" \
    build-essential \
    libpcre3-dev \
    libpq-dev \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip3 install --no-cache-dir -r ${APP_DIR}requirements.txt \
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Copy application code, wait-for-it.sh script to the container
COPY --chown=${APP_USER}:${APP_USER} ./src/ ./wait-for-it.sh ${APP_DIR}
RUN chmod +x ${APP_DIR}wait-for-it.sh

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

# Set the working directory
WORKDIR ${APP_DIR}

# uWSGI will listen on this port
EXPOSE 8000

ENTRYPOINT ["/bin/bash", "-c"]

# Start uWSGI
CMD ["uwsgi", "--ini", "uwsgi.ini"]
