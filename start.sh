#!/bin/bash

# load environment variables
if [ -f .env ]; then
  export $(cat .env | xargs)
fi

if [ "$DEPLOY" = "PROD" ]; then
  docker compose up web
else
    echo "define deployment mode in .env"
fi