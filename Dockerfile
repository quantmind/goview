FROM python:3.6

WORKDIR /goview

RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get install -y \
        locales

ENV DOCKER true
ENV PYTHONPATH $PYTHONPATH:/goview
ENV LANG en_US.UTF-8


ADD . /goview
#
# INSTALL python dependencies & test
RUN ./scripts/install.sh
#
# Default ports
EXPOSE 7000

ENTRYPOINT ["./scripts/docker-entrypoint.sh"]
CMD ["scripts/serve.sh"]
