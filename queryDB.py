from data.database import Session
from data.models import Kodemon

session = Session()

if __name__ == "__main__":

    kodemonData = session.query(Kodemon).all()

    print "Printing Database content:\n"

    for elem in kodemonData:
        print elem.id
        print elem.execution_time
        print elem.timestamp
        print elem.token
        print elem.key, "\n"