FROM python:3.7-slim-stretch

USER root

RUN apt-get update -qq && apt-get install --no-install-recommends -y \
  sudo wget && apt-get clean

ENV uid 2000
ENV unpriv_user coder
ENV code_dir /opt/tests/

RUN adduser --disabled-password --shell /bin/bash --home ${code_dir} --gecos 'coder' --uid $uid $unpriv_user

COPY docker/start-app.sh /opt/start-app.sh
COPY tests/requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

USER $unpriv_user
WORKDIR $code_dir
ENTRYPOINT [ "/opt/start-app.sh" ]
