import socket
import pika

"""
Before the server is started for the first time after reset this
command needs to be executed in python with the virtualenv
enabled:

    from data.database import engine, Base
    from data.models import Kodemon
    Base.metadata.create_all(engine)
"""

# UDP Listen to UDP packets
UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listen_addr = ("localhost", 4000)
UDPSock.bind(listen_addr)

# Set up connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='Kodemon')

print "=== Server Stared ==="
while True:
    data, addr = UDPSock.recvfrom(1024)

    channel.basic_publish(exchange='',
                      routing_key='Kodemon',
                      body=data)
    print " [x] Sent message"


