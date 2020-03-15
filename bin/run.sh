#!/usr/bin/env bash

color_settings() {
    # Jenkins has mono output. Color escape chars mess output
    if [ -n "${JENKINS_URL}" ]; then
        echo "--no-color"
    fi
}

selenium() {
  export ADDRESS="$1"
  shift 2

  mkdir -p `dirname $0`/../tests/failed_scenarios_screenshots/feature_errors
  chmod 0777 `dirname $0`/../tests/failed_scenarios_screenshots/feature_errors
  mkdir -p `dirname $0`/../reports
  chmod 0777 `dirname $0`/../reports
  chmod 0777 `dirname $0`/../reports/*
  rm -f `dirname $0`/../tests/failed_scenarios_screenshots/feature_errors/*
  rm -f `dirname $0`/../reports/*.xml # clean report for multiple local runs

  docker-compose -f docker/docker-compose.yml build
  docker-compose -f docker/docker-compose.yml up $(color_settings) -d poligon
  docker-compose -f docker/docker-compose.yml run selenium-tests $@

  docker-compose -f docker/docker-compose.yml stop

}

while (( 1 )); do
  case "$1" in
    '-d')
      ADDRESS="$2"
      shift 2
      ;;
    *)
      break
      ;;
  esac
done

case "$1" in
  'tests')
    selenium "staging-qa.piwik.pro" ""  ${@:2}
    ;;
  'tests-local')
    selenium "$ADDRESS" "" "" ${@:2}
    ;;
esac
