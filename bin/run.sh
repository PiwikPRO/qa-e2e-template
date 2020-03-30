#!/usr/bin/env bash

selenium() {

  docker-compose -f docker/docker-compose.yml build
  docker-compose -f docker/docker-compose.yml up -d poligon
  docker-compose -f docker/docker-compose.yml run selenium-tests $@

  docker-compose -f docker/docker-compose.yml stop

}

case "$1" in
  'tests')
    selenium ${@:2}
    ;;
esac
