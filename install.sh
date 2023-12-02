#! /bin/bash

export AIRFLOW_HOME=`dirname $(realpath $0)\src`
echo $AIRFLOW_HOME

export AIRFLOW_VERSION=2.5.1
echo $AIRFLOW_VERSION 

export PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
echo $PYTHON_VERSION

export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
echo $CONSTRAINT_URL


pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
