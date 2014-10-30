import socket
import json

from data.models import Kodemon
from data.database import Session

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

# Set up database connection
session = Session()


print "=== Server Stared ==="
while True:
    data, addr = UDPSock.recvfrom(1024)

    # Format data to Json
    jData = json.loads(data)


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
