import pika
import json

from data.models import Kodemon
from data.database import Session

# Set up connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='Kodemon')

# Set up database connection
session = Session()


def callback(ch, method, properties, body):
    print " [x] Received function message"

    # Format data to Json
    jData = json.loads(body)


    # Makes the path stored in key relevant to "CodeMon"
    shortKey = jData["key"]
    shortKey = shortKey[shortKey.rfind("CodeMon") - 1:]

    # Create an object that will be put in the db
    kodemonData = Kodemon(execution_time = jData["execution_time"],
                          timestamp = jData["timestamp"],
                          token = jData["token"],
                          key = shortKey,
                          func_name = jData["func_name"],
                          filename = jData["filename"])

    session.add(kodemonData)
    session.commit()


# Register a "callback" as a callback function with RabbitMQ
channel.basic_consume(callback,
                      queue='functions',
                      no_ack=True)

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()