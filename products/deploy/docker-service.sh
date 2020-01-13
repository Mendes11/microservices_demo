#!/usr/bin/env bash

# wait for Postgres to start

function rabbit_ready(){
python << END
import sys
import pika

try:
	connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
	channel = connection.channel()
except:
	sys.exit(-1)
sys.exit(0)

END
}

until rabbit_ready; do
  >&2 echo "RabbitMq is unavailable - sleeping"
  sleep 1
done

nameko run services.service --config=services/config.yaml
