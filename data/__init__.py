from database import engine, Base
from models import Kodemon

Base.metadata.create_all(engine)