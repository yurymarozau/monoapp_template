FROM python:3.11.1-slim

# do not buffer output
ENV PYTHONUNBUFFERED 1

# do not write pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Create a group and user to run app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init --create-home -r -g ${APP_USER} ${APP_USER}

# Create project directory
ARG APP_DIR=/home/${APP_USER}/template
RUN mkdir ${APP_DIR} && chown ${APP_USER}:${APP_USER} ${APP_DIR}

# Copy requirements. application code, wait-for-it.sh script to the container
COPY --chown=${APP_USER}:${APP_USER} ./requirements.txt ./src/ ./wait-for-it.sh ${APP_DIR}
RUN chmod +x ${APP_DIR}/wait-for-it.sh

# Install python requirements
RUN pip3 install --no-cache-dir -r ${APP_DIR}/requirements.txt

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

# Set the working directory
WORKDIR ${APP_DIR}
