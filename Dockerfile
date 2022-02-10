FROM python:3.8-buster

# The enviroment variable ensures python output to the terminal without buffering
ENV PYTHONUNBUFFERED 1

RUN useradd --create-home appuser
USER appuser

RUN python -m venv /home/appuser/venv
# Make sure we use the virtualenv:
ENV PATH="/home/appuser/venv/bin:$PATH"

RUN mkdir /home/appuser/mediators
WORKDIR  /home/appuser/mediators

# copy the everything from host machine into the home directory of the container
COPY --chown=appuser . /home/appuser/mediators

COPY ./requirements.txt /home/appuser/mediators/

RUN  pip install --upgrade pip && pip install -r requirements.txt

# copy the entrypoint file from host machine into the home directory of the container
COPY --chown=appuser:appuser ./entrypoint.sh /home/appuser/mediators/entrypoint.sh
RUN chmod +x /home/appuser/mediators/entrypoint.sh
