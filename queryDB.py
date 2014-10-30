from data.database import Session
from data.models import Kodemon

session = Session()

if __name__ == "__main__":

    kodemonData = session.query(Kodemon).all()

    print "Printing Database content:\n"

    for elem in kodemonData:
        print elem.__str__()

